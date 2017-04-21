import re

def str_common_word(str1, str2, minLength=1, string_only=False):
    word_list=[]
    num=0
    total_entries=0
    cnt_letters=0
    cnt_unique_letters=0
    all_num=0
    all_total_entries=0
    all_cnt_letters=0
    for word in str1.split():
         if len(word)>=minLength:
             if string_only==False or len(re.findall(r'\d+', word))==0:
                 if (' '+word+' ') in (' '+str2+' '):
                     num+=1
                     total_entries+=(' '+str2+' ').count(' '+word+' ')
                     cnt_letters+=(' '+str2+' ').count(' '+word+' ') * (len(word))
                     cnt_unique_letters+=(len(word))
                     word_list.append(word)
                 all_num+=1
                 all_total_entries+=1
                 all_cnt_letters+=len(word)
    
    if all_num==0:
        ratio_num=0
    else:
        ratio_num=1.0*num/all_num
    
    if all_cnt_letters==0:
        ratio_letters=0
    else:
        ratio_letters=1.0*cnt_unique_letters/all_cnt_letters
                 
    return num, total_entries, cnt_unique_letters, ratio_num, ratio_letters, " ".join(word_list)


def str_whole_word(str1, str2, i_):
    cnt = 0
    while i_ < len(str2):
        i_ = str2.find(str1, i_)
        if i_ == -1:
            return cnt
        else:
            cnt += 1
            i_ += len(str1)
    return cnt

def query_brand_material_in_attribute(str_query_brands,str_attribute_brands):
    list_query_brands=list(set(str_query_brands.split(";")))
    list_attribute_brands=list(set(str_attribute_brands.split(";")))
    while '' in list_query_brands:
        list_query_brands.remove('')
    while '' in list_attribute_brands:
        list_attribute_brands.remove('')
    
    str_attribute_brands=" ".join(str_attribute_brands.split(";"))    
    full_match=0
    partial_match=0
    assumed_match=0
    no_match=0
    num_of_query_brands=len(list_query_brands)
    num_of_attribute_brands=len(list_attribute_brands)
    if num_of_query_brands>0:
        for brand in list_query_brands:
            if brand in list_attribute_brands:
                full_match+=1
            elif ' '+brand+' ' in ' '+str_attribute_brands+' ':
                partial_match+=1
            elif (' '+brand.split()[0] in ' '+str_attribute_brands and brand.split()[0][0] not in "0123456789") or \
            (len(brand.split())>1 and (' '+brand.split()[0]+' '+brand.split()[1]) in ' '+str_attribute_brands):
                assumed_match+=1
            else:
                no_match+=1
                
    convoluted_output=0 # no brand in query
    if num_of_query_brands>0:
        if num_of_attribute_brands==0:
            convoluted_output = -1 # no brand in text, but there is brand in query
        elif no_match==0:
            if assumed_match==0:
                convoluted_output=3 # all brands fully matched
            else:
                convoluted_output=2 # all brands matched at least partially
        else:
            if full_match+ partial_match+ assumed_match>0:
                convoluted_output = 1 # one brand matched but the other is not
            else:
                convoluted_output= -2  #brand mismatched
    
    return convoluted_output
    
def extract_after_word(s,word):
    output=""
    if word in s:
        srch= re.search(r'(?<=\b'+word+'\ )[a-zA-Z0-9\n\ \%\$\-\#\@\&\/\.\'\*\(\)\,]+',s)
        if srch!=None:
            output=srch.group(0)
    return output