import streamlit as st
from funcoe import dados, buscar_historico_bitcoin, converter

st.title ("💱Painel de Cotações")
# COLUNAS divide a tela em quadrantes 
col1,col2,col3,col4,= st.columns(4)
col1.metric("Dolar(USD)",f"R${dados['USDBRL']['bid']}")
col2.metric("Euro(EUR)",f"R${dados['EURBRL']['bid']}")
col3.metric("Bitcoin(BTC)",f"R${dados['BTCBRL']['bid']}")
col4.metric("Francos Suiço (CHF)",f"R${dados['CHFBRL']['bid']}")

# Gráfico
st.subheader("Variação do Bitcoin ")
historico = buscar_historico_bitcoin()

st.line_chart(historico)#transforma uma lista em um grafico 

# Histórico de conversões

if "historico" not in st.session_state:
    st.session_state.historico = []
valor = st.number_input("Digite o valor que deseja converter em reais ", min_value=0.0)
cotacao_dolar = float(dados['USDBRL']['bid'])

if st.button("Converter para Dolar"):
    valor_convertido = valor/cotacao_dolar
    st.session_state.historico.append(f"R${valor}-USD{valor_convertido:.2f}")

st.subheader("Historico de Converções")
for item in st.session_state.historico:
    st.write(item)

st.title("Conversor de Moedas")
aba1, aba2, aba3 =st.tabs(["Cotações", "Graficos","Conversão"])

with aba1:
    col1,col2,col3,col4, = st.columns(4)
    col1.metric("Dolar(USD)",f"R${dados['USDBRL']['bid']}")
    col2.metric("Euro(EUR)",f"R${dados['EURBRL']['bid']}")
    col3.metric("Bitcoin(BTC)",f"R${dados['BTCBRL']['bid']}")
    col4.metric("Francos Suiços (CHF)",f"R${dados['CHFBRL']['bid']}")
with aba2:
    st.line_chart(buscar_historico_bitcoin())
with aba3:
    valor= st.number_input("Valor que deseja converter em reais",min_value=0.0)
    moeda = st.selectbox("Converter para",["USD","EUR","ARS","CHF"])
    cotacao = float(dados[f"{moeda}BRL"]['bid'])
    if st.button("Converter"):
        resultado = converter(valor,cotacao)
        st.write(f"Valor da converção:{resultado:.2f}")
        st.session_state.historico.append(f"R${valor}{moeda}{resultado:.2f}")
