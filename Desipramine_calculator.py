
# coding: utf-8

# In[ ]:


#This is my first script!!!!! 

#This is a calculator for determining mg needed per volume of stock solution 
#This is a calculator for determining how much desipramine needs to be injected per mouse weight


# In[ ]:


###STOCK SOLUTION CALCULATOR###
#For preparing _____ mL of desipramine solution at _____ mg/mL concentration. 

vol_stock = float(input("What volume(mL) of desipramine would you like to make?"))
concentration_stock = float(input("What concentration(mg/mL) of despiramine would you like to make?"))

#MW of desipramine HCL: 302.84. MW of HCL: 36.46. MW of free base = 266.38 
#correction factor = 302.84/266.38 = 1.137 
correction = 1.137

mg_stock = concentration_stock * vol_stock * correction 
print ("To obtain concentration(mg/mL) of " + str(concentration_stock) + " in a volume(mL) of " + str(vol_stock) + " use " + str(mg_stock) + " mg ")


# In[ ]:


###INDIVIDUAL DOSE BY WEIGHT CALCULATOR###

weight_g = input("Mouse weight in g: ")
weight_kg = float(weight_g) / 1000

#dosage units are mg/kg 
#Our protocol: dose = 10mg/kg 

dose = float(input("Required dose (mg/kg):"))
mg_needed = weight_kg * 10 
vol_needed = mg_needed / concentration_stock

print ("Inject " + str(vol_needed) + "of desipramine at concentration(mg/ml) " + str(concentration_stock) + " for dose(mg/kg) " + str(dose))

convert = input("Convert to uL? input 'y' or 'n'")

if convert == 'y': 
    vol_needed = vol_needed * 1000
    print (vol_needed)
elif convert == 'n': 
    print ("ok")
else: 
    print ("not a valid input, try again")


