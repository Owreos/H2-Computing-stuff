```
**Begin**
Read Sus
IF Mark <= 39:
	PRINT 'Fail'
ELIF Mark 40 <= Mark <= 44:
	PRINT 'S'
ELIF Mark 45 <= Mark <= 49:   
	PRINT 'E'
ELIF Mark 50 <= Mark <= 54:
	PRINT 'D'
ELIF Mark 55 <= Mark <= 59:
	PRINT 'C'
ELIF Mark 60 <= Mark <= 69:
	PRINT 'B'
ELIF Mark 70 <= Mark <= 100:
	PRINT 'A'
ENDIF
**End**
```

```
**BEGIN**
    READ gross
    READ Dependant
    FTaxable = gross - 10 000 - 2000*Dependant
    IF FTaxable <= 0:
        print 'What Taxes?'
    ELSE:
        FTax = FTaxable*0.2
        print FTax
    ENDIF
**END**
```
Testcases:
Child:
gross = 0
Dependants = 0
Output: What Taxes?

Gross = 50000
Dependants = 2
Output = 7200

Gross = 14000
Dependants = 2
Output = What Taxes?
