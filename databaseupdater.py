import pandas as pd

# Create list to hold the new urls
new_urls=[]

# Open the malicious.txt as file handle
with open('malicious.txt','r') as fh:
    # Itera over all elements 
    for u in fh:
        # Add each element to the list
        new_urls.append(u.rstrip('\n'))
            
#print(new_urls[0:5])
# Get the number of urls 
tot=len(new_urls)

# Create a datframe object
df=pd.read_csv('urldata-Copy.csv',index_col=0)
# Define labels for columns C and D
label='malicious'
result=1

# Fill a dataframe with new entries
new_entries=pd.DataFrame({
    'url':new_urls,
    'label':[label]*tot,
    'result':[result]*tot
    })
    
# Join both datframes 
df=pd.concat([df,new_entries])    

# Output result as csv
df.to_csv('malware_database.csv')

print(df.tail())