text = "X-DSPAM-Confidence:    0.8475";


x=text.find('0')
y=x+7
print(float(text[x:y]))
