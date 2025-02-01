def years_invested(years:int, salary_monthly:int):
    cpf = 0
    savings = 0
    investments = 0
    year = 1
    res = []
    while year <= years:
        for month in range(12):
            cpf_int = cpf * (0.025/12)
            cpf = cpf + cpf_int + salary_monthly *0.37
            salary_post = salary_monthly*(1-0.20)
            
            savings_int = savings * (0.03/12)
            savings = savings + savings_int + salary_post*0.25
            investments_int = investments * (0.05/12)
            investments = investments + investments_int + salary_post*0.25
        res.append([year, round(cpf,0),round(savings,0),round(investments,0)])
        year +=1
    return res

print(years_invested(2,3500))