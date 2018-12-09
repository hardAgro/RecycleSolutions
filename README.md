SPD – System Pests Detector

Aplicativos:
RS_DataCollector.ino	//Aplicativo de Arduino que coleta dados dos sensores e publica num web server
RS_db.py			//Script em Python para captura os dados do web Server que roda no Arduino
RS_app.py			//Script em Python para alimentar o banco de dados  e o dashboard com os dados capturados
RS_setup.py			//Script de instalação do aplicativo no computador
Pré-requisitos App:
1 – Arduino IDE		//IDE para instalação do arquivo .ino;
2 – Python 3.6.5		//Interpretador da linguagem para rodar os scripts .py;
3 – SQLite 3			//Banco de dados para armazenar os dados
Instalação e execução App:
1 – Clone o projeto;
2 – Instale o RS_DataCollector.ino no Arduino;
3 – Use o RS_setup.py script para a instalação da plataforma e do banco de dados;
4 – Rode o RS_db.py;
5 – Rode o RS_app.py;
6 – Abra num browser a página HTTP://localhost:8001 para visualizar a plataforma
Features App:
1 – Armadilha inteligente que conta a quantidade de diferentes pragas, insetos que foram atraídos por diferentes feromônios ou por diferentes armadilhas (cores);
2 – Testa a qualidade de aplicação de defensivos no recobrimento das frutas e/ou alvos;
3 – A plataforma gerencia o controle fitossanitário mostrando os dados das armadilhas e do detector de qualidade de pulverização.

Licensas App:
Python (GLP)
SQLite (Software)
Arduino IDE (GLP)
