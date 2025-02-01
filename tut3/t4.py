def years_invested(years:int, salary_monthly:int, increment:int):
    cpf = 0
    savings = 0
    investments = 0
    year = 1
    res = []
    while year <= years:
        if year > 3:
            salary_monthly = salary_monthly * (1+increment/100)
            for month in range(1,13):
                cpf_int = cpf * (0.025/12)
                cpf = cpf + cpf_int + salary_monthly *0.37
                salary_post = salary_monthly*(1-0.20)
                
                savings_int = savings * (0.03/12)
                savings = savings + savings_int + salary_post*0.25
                
                investments_int = investments * (0.05/12)
                investments = investments + investments_int + salary_post*0.25
                
                if month % 3 == 0 and month != 1:
                    investments = investments * 1.02
                    
            res.append([year, round(cpf,0),round(savings,0),round(investments,0)])
        else:
            for month in range(1,13):
                cpf_int = cpf * (0.025/12)
                cpf = cpf + cpf_int + salary_monthly *0.37
                salary_post = salary_monthly*(1-0.20)
                
                savings_int = savings * (0.03/12)
                savings = savings + savings_int + salary_post*0.25
                investments_int = investments * (0.05/12)
                investments = investments + investments_int + salary_post*0.25
                
                if month % 3 == 0 and month != 1:
                    investments = investments * 1.02
            res.append([year, round(cpf,0),round(savings,0),round(investments,0)])
        year +=1
    return res

print(years_invested(4, 3500, 25))