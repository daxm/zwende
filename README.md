# ZWENDE
## Zero Width ENcoder DEcoder
The goal of this project is to provide a method to encode and decode "hidden" messages that are embedded within a normal text message.  
Two zero width characters are used to create a binary mechanism that is used to create the binary equivalent of Unicode characters.  
This encoded text is then embedded in a "message". 

## enzero
Encode the "hidden message" text into zero width characters that are then embedded in the "message" text.

```python
output = enzero(hidden_message, message)
```

## dezero
This will scrub the provided text for zero width characters and try to "decode" them using our enzero encoding method.

```python
hiddent_message = dezero(message)
```
