text = 'X-DSPAM-Confidence:    0.8475';

start = text.find('0')
end = text.find('5')

print float(text[start:end+1])