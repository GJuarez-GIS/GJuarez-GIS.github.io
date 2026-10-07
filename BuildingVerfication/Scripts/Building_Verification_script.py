#Expression:
Verified_Buildings(!SFA!, !SFD!, !M2TO4!, !M5PLUS!, !MOBILE!, !ADU_D!, !ADU_A!, !ADU_R!, !JADU!, !STRUC_TYPE!)



#Code Block:
 #def = definition this defines all of the fields that are going to be used within the Verified_Buildings field.
def Verified_Buildings(SFA, SFD, M2_4, M5PLUS, MOBILE, ADU_D, ADU_A, ADU_R, JADU, STRUC_TYPE):

#this defines if there is a value to return that value as long as it isn't a NUll, empty space, or a 0.   
    def has(value):
        return value not in (None,'', 0)
    
# parts is defined to to be included and joined if there is a value that is not stated above.
    parts=[]
    
# These are the Main Buildings. 
#if has() = if there is a value within this field.
#(str) = string and (int) = integer str(int(SFA))) will return whatever number is in the field as a integer 1 instead of a text 1.0.
    if has (SFA):
        parts.append("SFA," + str(int(SFA)))
    if has (SFD):
        parts.append("SFD," + str(int(SFD)))
    if has (M2_4):
        parts.append("M2_4," + str(int(M2_4)))
    if has (M5PLUS):
        parts.append("M5PLUS," + str(int(M5PLUS)))
    if has (MOBILE):
        parts.append("MOBILE,"+ str(int(MOBILE)))
        
# These are the ADUs.
    if has (ADU_D):
        parts.append("ADU_D," + str(int(ADU_D)))
    if has (ADU_A):
        parts.append("ADU_A," + str(int(ADU_A)))
    if has (ADU_R):
        parts.append("ADU_R," + str(int(ADU_R)))
    if has(JADU):
        parts.append("JADU," + str(int(JADU)))
        
    if not parts and STRUC_TYPE not in (None, "", 0):
       return STRUC_TYPE

# if not data in any cell return <Null>
    if not parts:
       return None
    
# .join(parts) = brings all the values together such as (SFD,1, ADU_D,1).        
    return "," .join(parts)
