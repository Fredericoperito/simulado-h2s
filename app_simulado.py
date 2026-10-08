import streamlit as st

st.set_page_config(page_title="Simulado Tático H2S", layout="wide")

if 'fase' not in st.session_state:
    st.session_state.fase = 'pre_jogo'

def mudar_fase(nova_fase):
    st.session_state.fase = nova_fase

# ==========================================
# FASE ZERO: PRÉ-JOGO
# ==========================================
if st.session_state.fase == 'pre_jogo':
    st.title("Simulado Tático: Emergência com H₂S")
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.markdown("""
        ### O Cenário
        **Sexta-feira, 18h30.** O ambiente está controlado. A equipe prepara-se para iniciar o experimento.
        O laboratório possui um cilindro de Sulfeto de Hidrogênio (H₂S) fora da capela de exaustão.
        """)
        st.write("Equipamentos disponíveis no corredor: 1 EPRA (SCBA) e máscaras de filtro VO/GA.")
        st.write("---")
        if st.button("⚠️ INICIAR EXPERIMENTO", use_container_width=True):
            mudar_fase('inicio')
            st.rerun()
            
    with col_imagem:
        st.image("media/lab_normal.jpg", use_container_width=True)

# ==========================================
# FASE 1: O INCIDENTE
# ==========================================
elif st.session_state.fase == 'inicio':
    st.title("Rodada 1: O Incidente Base")
    
    st.audio("media/alarme.mp3", format="audio/mp3", autoplay=True, loop=True)
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.markdown("""
        **Sexta-feira, 18h45.** Ouve-se um estalo alto e o gás pressurizado vaza. 
        O Pesquisador 1 tenta fechar a válvula e colapsa no chão.
        
        *10 segundos depois, o cheiro forte de ovo podre parece desaparecer (Fadiga Olfativa).*
        """)
        
        st.subheader("O que a equipe faz?")
        if st.button("A) Vestir máscaras de filtro e entrar para o resgate", use_container_width=True):
            mudar_fase('A')
            st.rerun()
        if st.button("B) Fugir em pânico e deixar a porta aberta", use_container_width=True):
            mudar_fase('B')
            st.rerun()
        if st.button("C) Bater a porta, isolar a área e vestir EPRA", use_container_width=True):
            mudar_fase('C')
            st.rerun()
            
    with col_imagem:
        st.image("media/lab_vazamento.jpg", use_container_width=True)

# ==========================================
# CAMINHO A: A ARMADILHA DO FILTRO
# ==========================================
elif st.session_state.fase == 'A':
    st.title("Decisão Crítica: Uso de Filtros")
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.error("⚠️ ALERTA TÁTICO")
        st.write("A equipe entra na Zona Quente. Em 15 segundos, o carvão do filtro satura na concentração letal (IDLH). O H₂S começa a invadir as máscaras.")
        
        st.subheader("O gás afeta a coordenação. Qual a reação instintiva?")
        if st.button("A1) Tentar puxar todos os caídos sozinho (Força Bruta)", use_container_width=True):
            mudar_fase('A1')
            st.rerun()
        if st.button("A3) Correr e pedir ajuda a outros colegas exaustos", use_container_width=True):
            mudar_fase('A3')
            st.rerun()
            
    with col_imagem:
        st.image("media/A_decisao_filtro.jpg", use_container_width=True)

elif st.session_state.fase == 'A1':
    st.title("Resultado da Intervenção")
    st.audio("media/game_over.mp3", format="audio/mp3", autoplay=True)
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.error("💀 GAME OVER: O Mártir")
        st.write("O esforço físico extremo multiplica a taxa de respiração. A saturação é fulminante. A equipe inteira sucumbe, transformando um incidente local num Desastre de Múltiplas Vítimas.")
        st.write("---")
        if st.button("🔄 Jogar Novamente", use_container_width=True):
            mudar_fase('pre_jogo')
            st.rerun()
            
    with col_imagem:
        st.image("media/A1_o_martir.jpg", use_container_width=True)

elif st.session_state.fase == 'A3':
    st.title("Resultado da Intervenção")
    st.audio("media/game_over.mp3", format="audio/mp3", autoplay=True)
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.error("💀 GAME OVER: Recrutamento Fatal")
        st.write("Colegas exaustos do laboratório vizinho são recrutados. O uso de filtros VO/GA e a respiração ofegante devido ao stress saturam as máscaras em segundos. Todos colapsam na Zona Quente.")
        st.write("---")
        if st.button("🔄 Jogar Novamente", use_container_width=True):
            mudar_fase('pre_jogo')
            st.rerun()
            
    with col_imagem:
        st.image("media/A3_recrutamento.jpg", use_container_width=True)

# ==========================================
# CAMINHO B: A FUGA EM PÂNICO
# ==========================================
elif st.session_state.fase == 'B':
    st.title("Decisão: Abandono da Zona Quente")
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.error("⚠️ ALERTA DE PROPAGAÇÃO")
        st.write("A equipe foge e deixa a porta do laboratório escancarada. O gás pesado começa a vazar para o corredor, estratificando no chão e ameaçando todo o andar.")
        
        st.subheader("No corredor, qual a atitude da equipe?")
        if st.button("B1) Continuar fugindo pelas escadas sem avisar ninguém", use_container_width=True):
            mudar_fase('B1')
            st.rerun()
        if st.button("B2) Acionar o alarme de incêndio padrão", use_container_width=True):
            mudar_fase('B2')
            st.rerun()
        if st.button("B3) Bloquear a escada e atuar como Comandante Tático", use_container_width=True):
            mudar_fase('B3')
            st.rerun()
            
    with col_imagem:
        st.image("media/B_fuga_corredor.jpg", use_container_width=True)

elif st.session_state.fase == 'B1':
    st.title("Resultado da Intervenção")
    st.audio("media/game_over.mp3", format="audio/mp3", autoplay=True)
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.error("💀 GAME OVER: Omissão de Dados")
        st.write("A segurança do campus e outros alunos entram no andar sem proteção respiratória. O gás invisível e inodoro (devido à fadiga olfativa) no corredor causa múltiplas vítimas fatais secundárias.")
        st.write("---")
        if st.button("🔄 Jogar Novamente", use_container_width=True):
            mudar_fase('pre_jogo')
            st.rerun()
            
    with col_imagem:
        st.image("media/B1_omissao_dados.jpg", use_container_width=True)

elif st.session_state.fase == 'B2':
    st.title("Resultado da Intervenção")
    st.audio("media/game_over.mp3", format="audio/mp3", autoplay=True)
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.error("💀 GAME OVER: Informação Falsa")
        st.write("As guarnições de bombeiros chegam preparadas para um princípio de incêndio estrutural comum. Avançam pelo corredor denso de H₂S sem EPRA equipado. A primeira equipa de ataque cai em segundos.")
        st.write("---")
        if st.button("🔄 Jogar Novamente", use_container_width=True):
            mudar_fase('pre_jogo')
            st.rerun()
            
    with col_imagem:
        st.image("media/B2_info_falsa.jpg", use_container_width=True)

elif st.session_state.fase == 'B3':
    st.title("Resultado da Intervenção")
    st.audio("media/sucesso.mp3", format="audio/mp3", autoplay=True)
    st.balloons()
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.success("🏆 SUCESSO: Comando e Contenção")
        st.write("Apesar do abandono inicial da porta, o cientista assume uma postura tática. Ele bloqueia o acesso ao andar e informa os Bombeiros e o GOPP via rádio sobre a presença exata de H₂S. O socorro já entra com proteção adequada.")
        st.write("---")
        if st.button("🔄 Reiniciar Simulação", use_container_width=True):
            mudar_fase('pre_jogo')
            st.rerun()
            
    with col_imagem:
        st.image("media/B3_dados_criticos.jpg", use_container_width=True)

# ==========================================
# CAMINHO C: ISOLAMENTO TÁTICO
# ==========================================
elif st.session_state.fase == 'C':
    st.title("Decisão: Zona Quente Contida")
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.success("✅ DECISÃO TÁTICA CORRETA")
        st.write("A porta fechada contém temporariamente o volume do gás pesado. O resto do prédio ganha tempo para evacuar. O cientista mais experiente veste o EPRA (SCBA).")
        
        st.subheader("Ação do Operador com SCBA:")
        if st.button("C1: Correr para tentar fechar a válvula do cilindro", use_container_width=True):
            mudar_fase('C1')
            st.rerun()
        if st.button("C2: Ignorar a válvula e fazer a Extração Tática do colega", use_container_width=True):
            mudar_fase('C2')
            st.rerun()
        if st.button("C3: Iniciar RCP no colega caído dentro do laboratório", use_container_width=True):
            mudar_fase('C3')
            st.rerun()
            
    with col_imagem:
        st.image("media/lab_vazamento.jpg", use_container_width=True)

elif st.session_state.fase == 'C1':
    st.title("Resultado da Intervenção")
    st.audio("media/game_over.mp3", format="audio/mp3", autoplay=True)
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.error("💀 GAME OVER: Conter a Fonte")
        st.write("O operador priorizou o equipamento ao invés da vida. O tempo de 30 a 40 segundos gasto tentando fechar uma válvula danificada custou a oxigenação cerebral do colega. Vítima em PCR irreversível.")
        st.write("---")
        if st.button("🔄 Jogar Novamente", use_container_width=True):
            mudar_fase('pre_jogo')
            st.rerun()
            
    with col_imagem:
        st.image("media/C1_conter_fonte.jpg", use_container_width=True)

elif st.session_state.fase == 'C2':
    st.title("Resultado da Intervenção")
    st.audio("media/sucesso.mp3", format="audio/mp3", autoplay=True)
    st.balloons()
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.success("🏆 SUCESSO ABSOLUTO: Extração Tática")
        st.write("Protocolo 'Life Safety' aplicado com perfeição. O operador entra, arrasta a vítima para o corredor (área fria) em menos de 10 segundos e sela a porta novamente. A RCP é iniciada com sucesso em ambiente seguro.")
        st.write("---")
        if st.button("🔄 Reiniciar Simulação", use_container_width=True):
            mudar_fase('pre_jogo')
            st.rerun()
            
    with col_imagem:
        st.image("media/C2_extracao_tatica.jpg", use_container_width=True)

elif st.session_state.fase == 'C3':
    st.title("Resultado da Intervenção")
    st.audio("media/game_over.mp3", format="audio/mp3", autoplay=True)
    
    col_texto, col_imagem = st.columns([1, 1.5])
    
    with col_texto:
        st.error("💀 GAME OVER: RCP Interna")
        st.write("O operador tenta prestar socorro na Zona Quente e afasta levemente a própria máscara (quebra de selo) para tentar ventilar o colega. Inalação fulminante de H₂S. Ambos morrem no local.")
        st.write("---")
        if st.button("🔄 Jogar Novamente", use_container_width=True):
            mudar_fase('pre_jogo')
            st.rerun()
            
    with col_imagem:
        st.image("media/C3_rcp_interna.jpg", use_container_width=True)