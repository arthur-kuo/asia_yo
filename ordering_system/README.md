

## SOLID

### SRP:
	1. validator.py中, 每種Validator只負責單一種類的驗證
	2. currency.py中, 實作CurrencyConverter只用於貨幣轉換

### OCP:
	1. currency.py中,雖然目前只接受TWD與USD,但不排除未來新增多種貨幣, 可以在exchange_rate.py中新增貨幣種類與匯率, 不需要修改舊的程式碼
	2. /app/routers/index.py中, 未來建立新的router時,只要引用新的router即可,不需要修改舊的程式碼

### ISP:
	1. validator.py中, 藉由繼承IValidator實作出各種Validator, 當未來需要增加其他驗證項目時,可直接新增或取用需要的Validator, 不會存在不需要的方法


## Design Pattern


### Strategy Pattern:
	1. currency.py中, 藉由封裝各種



## PS.
	1. 把exchange_rate單獨拿出來建立一個file是因為, 未來匯率有變動時, 單獨編輯該文檔即可, 爬蟲也可以比較好串接


