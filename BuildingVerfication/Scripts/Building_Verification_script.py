#Expression:
Verified_Buildings(!SFA20!, !SFD20!, !M2TO420!, !M5PLUS20!, !MOBILE20!, !ADU_D_20!, !ADU_A_20!, !ADU_R_20!, !JADU20!, !STRUC_TYPE_22!)



#Code Block:
 #def = definition this defines all of the fields that are going to be used within the Verified_Buildings field.
def Verified_Buildings(SFA20, SFD20, M2TO420, M5PLUS20, MOBILE20, ADU_D_20, ADU_A_20, ADU_R_20, JADU20, STRUC_TYPE_22):

#this defines if there is a value to return that value as long as it isn't a NUll, empty space, or a 0.   
    def has(value):
        return value not in (None,'', 0)
    
# parts is defined to to be included and joined if there is a value that is not stated above.
    parts=[]
    
# These are the Main Buildings. 
#if has() = if there is a value within this field.
#(str) = string and (int) = integer str(int(SFA20))) will return whatever number is in the field as a integer 1 instead of a text 1.0.
    if has (SFA20):
        parts.append("SFA," + str(int(SFA20)))
    if has (SFD20):
        parts.append("SFD," + str(int(SFD20)))
    if has (M2TO420):
        parts.append("M2TO4," + str(int(M2TO420)))
    if has (M5PLUS20):
        parts.append("M5PLUS," + str(int(M5PLUS20)))
    if has (MOBILE20):
        parts.append("MOBILE,"+ str(int(MOBILE20)))
        
# These are the ADUs.
    if has (ADU_D_20):
        parts.append("ADU_D," + str(int(ADU_D_20)))
    if has (ADU_A_20):
        parts.append("ADU_A," + str(int(ADU_A_20)))
    if has (ADU_R_20):
        parts.append("ADU_R," + str(int(ADU_R_20)))
    if has(JADU20):
        parts.append("JADU," + str(int(JADU20)))
        
    if not parts and STRUC_TYPE_22 not in (None, "", 0):
       return STRUC_TYPE_22

# if not data in any cell return <Null>
    if not parts:
       return None
    
# .join(parts) = brings all the values together such as (SFD,1, ADU_D,1).        
    return "," .join(parts)

