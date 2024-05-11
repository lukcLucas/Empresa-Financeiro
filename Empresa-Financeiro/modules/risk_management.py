def assess_risk(portfolio):
    # Avaliação simplificada do risco baseada na alocação
    if portfolio['Allocation'].max() > 0.5:
        return "High Risk"
    return "Low Risk"

def simulate_market_scenario(asset, change_factor):
    # Simulação simplificada de um cenário de mercado
    print(f"Simulating market scenario for {asset}: {change_factor * 100}% change")
