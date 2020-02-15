def base2base(query,q_base,a_base):
    """Use this to perform base conversions from base-2 to base-20
    answers are in strings
    answers are not prefixed, such as 0b1100 or 0xFF...
    ....because author doesn't not what the prefix for other bases are!
    
    see codes for workings, it pretty simple.
    
    author: Wei Chong 11/2/2020 16:54pm BST"""
    if q_base<2 or q_base>21 or a_base<2 or a_base>21:
        print('Base converter only works from binary to base-20')
        return None
    elif q_base==a_base:
        return query
    elif q_base==10:
        if a_base>10:
            return dec2higher(query,base=a_base)
        else:
            return dec2lower(query,base=a_base)
    elif a_base>10:
        return dec2higher(base2dec(query,q_base),base=a_base)
    else:
        return dec2lower(base2dec(query,q_base),base=a_base) 
		
def dec2higher(query,base=16):
    """this function to change any decimal numbers (base 10) into 
    bases 10 (but why would you want to) to higher but only up to base 20
    
    limitations:
        it only works with integers, no fractions yet
        must start from Decimals (base 10)"""
    #Wei Chong 2020/02/11
    
    #a list to store final hex value, note because using append method, final result will be 
    #reversed
    hex_list=[]
    answer='0x'
    
    #initialise
    remainder=query
    d_value=query

    p=1 #power of base value
    brk=False

    while brk==False:
 
        remainder=d_value%base
        hex_list.append(hibasealfa(remainder))
        d_value=d_value//base

        #check when to stop
        if query/(base**p)<1:
            brk=True
        else:
            p+=1
            
    for i,j in enumerate(hex_list):
        if i==0:
            answer=str(hex_list[i])
        else:
            answer=str(hex_list[i])+answer

    return answer

def dec2lower(query,base=2):
    """converts from base 10 to binary
        current limitations:
            only converts from Decimals (base 10) to lower bases"""
    
    p=1 #initialise power of the target base 
    #base=2 #binary
    brk=False #for use with while loop
    remainder=query
    d_value=query
    
    bin_list=[] #list containing answers in reverse order
    
    while brk==False:
        remainder=d_value%base
        bin_list.append(remainder)
        d_value=d_value//base
        if query/(base**p) <1: #checks if loop should stop
            brk=True
        else:
            p+=1
    
    for i,j in enumerate(bin_list):
        if i==0:
            answer=str(bin_list[i])
        else:
            answer=str(bin_list[i])+answer
        
    return answer
def base2dec(query,q_base):
    """change from any base to decimals"""
    query=list(str(query))
    power=len(query)-1 #initialised the exponential for query base
    answer=0
    base10=0

    for i,char in enumerate(query):
        i_10=(hibasealfa(char))
        i_10p=(i_10*(q_base**power))
        if i_10<q_base:
            base10+=i_10p
        else:
            print('query value does not match base')
            return None
        power-=1
    return base10
def hibasealfa(number):
    """
    Returns the numbers for higher bases, eg. hibasealfa(11) returns string 'b'
    only works for numbers 0 to 20
    
    don't use this for quick hex conversion, it will not work correctly: 
    for example if you are looking to convert 17 to hex...
            hibasealfa(17) will result in ='h' and not 0x11"""
    
    chk_list=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','10','11','12','13','14','15','16',
              '17','18','19','20',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    bs20={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',
                  6:'6',7:'7',8:'8',9:'9',10:'a',
                  11:'b',12:'c',13:'d',14:'e',15:'f',
                 16:'g',17:'h',18:'i',19:'j',20:'k','0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
          '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, 'g':16, 'h':17, 'i':18, 'j':19, 'k':20}
    if number not in chk_list:
        print('unexpected character')
    else:
        return bs20.get(number)