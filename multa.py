from datetime import date

def calcular_valor_com_multa(valor_original: float, data_vencimento_str: str, taxa_multa_diaria_percentual: float = 2.5) -> dict:
    """
    Calcula o valor da multa (2.5% ao dia) com base na data de vencimento.
    A data deve ser informada no formato 'YYYY-MM-DD'.
    """
    try:
        data_vencimento = date.fromisoformat(data_vencimento_str)
        data_hoje = date.today()
        
        if data_hoje <= data_vencimento:
            return {
                "dias_atraso": 0,
                "valor_multa": 0.00,
                "valor_total": valor_original,
                "status": "Pagamento no prazo."
            }

        dias_atraso = (data_hoje - data_vencimento).days
        taxa_multa_diaria = taxa_multa_diaria_percentual / 100
        
        # Valor da multa total (Valor * Taxa diária * Dias de Atraso)
        valor_multa = valor_original * taxa_multa_diaria * dias_atraso
        valor_total = valor_original + valor_multa

        return {
            "dias_atraso": dias_atraso,
            "valor_multa": round(valor_multa, 2),
            "valor_total": round(valor_total, 2),
            "status": "Em Atraso"
        }
    
    except ValueError:
        return {"status": "Erro: Formato de data inválido. Use YYYY-MM-DD."}


if __name__ == "__main__":
    VALOR = 1000.00
    # Data de Vencimento de Exemplo (Ajuste para testar o atraso)
    DATA_VENCIMENTO_EXEMPLO = "2025-10-25" 

    resultado = calcular_valor_com_multa(VALOR, DATA_VENCIMENTO_EXEMPLO)

    print("\n--- Cálculo de Multa por Atraso ---")
    print(f"Valor Original: R${VALOR:.2f}")
    print(f"Data Vencimento: {DATA_VENCIMENTO_EXEMPLO}")
    print(f"Taxa de Multa Diária: 2.5%")

    print("\n**Resultado:**")
    if resultado['status'] == "Em Atraso":
        print(f"Status: **{resultado['status']}**")
        print(f"Dias de Atraso: **{resultado['dias_atraso']}** dias")
        print(f"Valor da Multa: **R${resultado['valor_multa']:.2f}**")
        print(f"Valor Total a Pagar: **R${resultado['valor_total']:.2f}**")
    else:
        print(f"Status: **{resultado['status']}**")
        print(f"Valor Total a Pagar: **R${resultado['valor_total']:.2f}**")