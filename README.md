# diffline
The program shows which characters have changed between two lines.

## usage
For use with static files:
```
cat myText.txt | ./diffline.py
```

For use with files that are constantly appended:
```
tail -f myText.txt | ./diffline.py
```

You can also use it with any pipe:
```
ls -l | ./diffline.py
```

## setup

```
pip install -r requirements.txt
```
