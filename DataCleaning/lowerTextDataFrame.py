lyrics=['Shine bright like a diamond'
'Shine bright like a diamond',
'Find light in the beautiful sea',
'I choose to be happy',
'You and I, you and I',
'We re like diamonds in the sky'
"You're a shooting star I see",
"A vision of ecstasy",
"When you hold me, I'm alive",
"We're like diamonds in the sky"]

print(lyrics)
#convert list lyrics to dataframe

from filecmp import clear_cache
import pandas as pd

df = pd.DataFrame({"lyrics": lyrics })
print(df.head())


#execute lower function on the text data

#example on simple text
x = "tesTing"
x2 = x.lower()
print(x2)

print(df.head())
print(df.columns)

print(df['lyrics'])
df["lyrics"] = df["lyrics"].apply(lambda x : " ".join(x.lower() for x in x.split()))
