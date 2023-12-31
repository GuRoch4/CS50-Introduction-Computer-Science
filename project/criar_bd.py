import sqlite3

# Função para conectar ao banco de dados SQLite
def conectar_bd():
    return sqlite3.connect('words.db')


# Lista de palavras a serem inseridas no banco de dados
actions_activities = [
    ('run', 'correr'),
    ('eat', 'comer'),
    ('talk', 'falar'),
    ('walk', 'andar'),
    ('work', 'trabalhar'),
    ('play', 'jogar'),
    ('read', 'ler'),
    ('write', 'escrever'),
    ('drive', 'dirigir'),
    ('sleep', 'dormir'),
    ('cook', 'cozinhar'),
    ('clean', 'limpar'),
    ('dance', 'dançar'),
    ('study', 'estudar'),
    ('sing', 'cantar'),
    ('watch', 'assistir'),
    ('listen', 'ouvir'),
    ('exercise', 'exercitar'),
    ('swim', 'nadar'),
    ('create', 'criar'),
    ('relax', 'relaxar'),
    ('volunteer', 'voluntário'),
    ('travel', 'viajar'),
    ('laugh', 'rir'),
    ('hug', 'abraçar'),
    ('kiss', 'beijar'),
    ('text', 'texto'),
    ('paint', 'pintar'),
    ('draw', 'desenhar'),
    ('teach', 'ensinar'),
    ('learn', 'aprender'),
    ('dress', 'vestir'),
    ('undress', 'despir'),
    ('brush', 'escovar'),
    ('shave', 'barbear'),
    ('bathe', 'banhar'),
    ('nap', 'cochilar'),
    ('type', 'digitar'),
    ('call', 'chamar'),
    ('visit', 'visitar'),
    ('bike', 'bicicleta'),
    ('skate', 'skate'),
    ('explore', 'explorar'),
    ('plan', 'planejar'),
    ('organize', 'organizar'),
    ('fix', 'consertar'),
    ('arrange', 'arranjar'),
    ('schedule', 'agendar'),
    ('feed', 'alimentar'),
    ('music', 'música'),
    ('make', 'fazer'),
    ('declutter', 'organizar'),
    ('donate', 'doar'),
    ('practice', 'praticar'),
    ('review', 'revisar'),
    ('revise', 'rever'),
    ('memorize', 'memorizar'),
    ('recite', 'recitar'),
    ('stretch', 'alongar'),
    ('jump', 'pular'),
    ('skip', 'pular'),
    ('balance', 'equilibrar'),
    ('lift', 'levantar'),
    ('carry', 'carregar'),
    ('drag', 'arrastar'),
    ('push', 'empurrar'),
    ('pull', 'puxar'),
    ('slide', 'deslizar'),
    ('turn', 'virar'),
    ('spin', 'girar'),
    ('bend', 'dobrar'),
    ('sit', 'sentar'),
    ('stand', 'ficar de pé'),
    ('lie', 'mentir'),
    ('roll', 'rolar'),
    ('crawl', 'rastejar'),
    ('squat', 'agachar'),
    ('sneeze', 'espirrar'),
    ('cough', 'tosse'),
    ('yawn', 'bocejar'),
    ('blink', 'piscar'),
    ('shake', 'balançar'),
    ('point', 'apontar'),
    ('wave', 'acenar'),
    ('hesitate', 'vacilar'),
    ('decide', 'decidir'),
    ('question', 'questionar')
]

emotions_feelings= [
    ('Happy', 'Feliz'),
    ('Sad', 'Triste'),
    ('Love', 'Amor'),
    ('Anger', 'Raiva'),
    ('Fear', 'Medo'),
    ('Excited', 'Animado'),
    ('Confused', 'Confuso'),
    ('Surprised', 'Surpreso'),
    ('Calm', 'Calmo'),
    ('Hopeful', 'Esperançoso'),
    ('Joy', 'Alegria'),
    ('Affection', 'Afeição'),
    ('Hatred', 'Ódio'),
    ('Anxiety', 'Ansiedade'),
    ('Disgust', 'Nojo'),
    ('Enthusiasm', 'Entusiasmo'),
    ('Contentment', 'Contentamento'),
    ('Agitated', 'Agitado'),
    ('Depressed', 'Deprimido'),
    ('Optimistic', 'Otimista'),
    ('Pessimistic', 'Pessimista'),
    ('Euphoria', 'Euforia'),
    ('Compassion', 'Compaixão'),
    ('Resentment', 'Ressentimento'),
    ('Surprise', 'Surpresa'),
    ('Satisfaction', 'Satisfação'),
    ('Disappointment', 'Desapontamento'),
    ('Ecstasy', 'Êxtase'),
    ('Longing', 'Saudade'),
    ('Guilt', 'Culpa'),
    ('Shame', 'Vergonha'),
    ('Overwhelmed', 'Sobrecarregado'),
    ('Grateful', 'Grato'),
    ('Delighted', 'Encantado'),
    ('Nostalgia', 'Nostalgia'),
    ('Frustration', 'Frustração'),
    ('Amusement', 'Diversão'),
    ('Sentimental', 'Sentimental'),
    ('Envy', 'Inveja'),
    ('Affectionate', 'Afetuoso'),
    ('Empathy', 'Empatia'),
    ('Repulsion', 'Repulsa'),
    ('Contempt', 'Desprezo'),
    ('Despair', 'Desespero'),
    ('Exhilaration', 'Exaltação'),
    ('Bitterness', 'Amargura'),
    ('Cheerful', 'Alegre'),
    ('Melancholy', 'Melancolia'),
    ('Irritated', 'Irritado'),
    ('Serene', 'Sereno'),
    ('Amazed', 'Surpreso'),
    ('Regret', 'Arrependimento'),
    ('Jealousy', 'Ciúme'),
    ('Tenderness', 'Ternura'),
    ('Hesitant', 'Vacilante'),
    ('Zeal', 'Zelo'),
    ('Disheartened', 'Desanimado'),
    ('Exuberant', 'Exuberante'),
    ('Humbled', 'Humilde'),
    ('Devastated', 'Devastado'),
    ('Thrilled', 'Animado'),
    ('Astonished', 'Espantado'),
    ('Sympathy', 'Simpatia'),
    ('Distressed', 'Aflito'),
    ('Enraged', 'Enfurecido'),
    ('Disillusioned', 'Desiludido'),
    ('Wistful', 'Saudoso'),
    ('Heartbroken', 'Despedaçado'),
    ('Astonishment', 'Espanto'),
    ('Aggravated', 'Agravado'),
    ('Optimism', 'Otimismo'),
    ('Sarcasm', 'Sarcasmo'),
    ('Discouraged', 'Desencorajado'),
    ('Delight', 'Deleite'),
    ('Uneasy', 'Inquieto'),
    ('Gleeful', 'Contente'),
    ('Discontent', 'Descontentamento'),
    ('Despondent', 'Desanimado'),
    ('Afflicted', 'Aflito'),
    ('Comforted', 'Confortado'),
    ('Displeased', 'Descontente'),
    ('Yearning', 'Anseio'),
    ('Apprehensive', 'Aprensivo'),
    ('Indignant', 'Indignado'),
    ('Voracious', 'Voraz'),
    ('Enchantment', 'Encantamento'),
    ('Hysteria', 'Histeria'),
    ('Repentant', 'Arrependido'),
    ('Agony', 'Agonia'),
    ('Eager', 'Ansioso'),
    ('Disenchanted', 'Desencantado'),
    ('Flustered', 'Confuso'),
    ('Tranquil', 'Tranquilo')
]

family_relationship = [
    ('Family', 'Família'),
    ('Friend', 'Amigo'),
    ('Mother', 'Mãe'),
    ('Father', 'Pai'),
    ('Brother', 'Irmão'),
    ('Sister', 'Irmã'),
    ('Husband', 'Marido'),
    ('Wife', 'Esposa'),
    ('Son', 'Filho'),
    ('Daughter', 'Filha'),
    ('Parents', 'Pais'),
    ('Grandfather', 'Avô'),
    ('Grandmother', 'Avó'),
    ('Grandparents', 'Avós'),
    ('Grandson', 'Neto'),
    ('Granddaughter', 'Neta'),
    ('Uncle', 'Tio'),
    ('Aunt', 'Tia'),
    ('Nephew', 'Sobrinho'),
    ('Niece', 'Sobrinha'),
    ('Cousin', 'Primo'),
    ('In-Laws', 'Sogros'),
    ('Father-in-law', 'Sogro'),
    ('Mother-in-law', 'Sogra'),
    ('Brother-in-law', 'Cunhado'),
    ('Sister-in-law', 'Cunhada'),
    ('Godfather', 'Padrinho'),
    ('Godmother', 'Madrinha'),
    ('Godson', 'Afilhado'),
    ('Goddaughter', 'Afilhada'),
    ('Stepfather', 'Padrasto'),
    ('Stepmother', 'Madrasta'),
    ('Stepbrother', 'Meio irmão'),
    ('Stepsister', 'Meia irmã'),
    ('Adoptive parents', 'Pais adotivos'),
    ('Adopted child', 'Filho adotivo'),
    ('Guardian', 'Tutor'),
    ('Ward', 'Tutelado'),
    ('Nanny', 'Babá'),
    ('Caregiver', 'Cuidador'),
    ('Orphan', 'Órfão'),
    ('Family tree', 'Árvore genealógica'),
    ('Ancestor', 'Antepassado'),
    ('Descendant', 'Descendente'),
    ('Lineage', 'Linhagem'),
    ('Relatives', 'Parentes'),
    ('Relationship', 'Relacionamento'),
    ('Marriage', 'Casamento'),
    ('Engagement', 'Noivado'),
    ('Wedding', 'Casamento'),
    ('Divorce', 'Divórcio'),
    ('Separation', 'Separação'),
    ('Love', 'Amor'),
    ('Affection', 'Afeição'),
    ('Support', 'Apoio'),
    ('Trust', 'Confiança'),
    ('Connection', 'Conexão'),
    ('Harmony', 'Harmonia'),
    ('Unity', 'União'),
    ('Communication', 'Comunicação'),
    ('Understanding', 'Compreensão'),
    ('Respect', 'Respeito'),
    ('Loyalty', 'Lealdade'),
    ('Devotion', 'Devoção'),
    ('Patience', 'Paciência'),
    ('Forgiveness', 'Perdão'),
    ('Empathy', 'Empatia'),
    ('Compassion', 'Compaixão'),
    ('Gratitude', 'Gratidão'),
    ('Joy', 'Alegria'),
    ('Togetherness', 'União'),
    ('Celebration', 'Celebração'),
    ('Reunion', 'Reunião'),
    ('Birth', 'Nascimento'),
    ('Childhood', 'Infância'),
    ('Parenting', 'Paternidade')
]

descriptive_words = [
    ('Big', 'Grande'),
    ('Small', 'Pequeno'),
    ('Good', 'Bom'),
    ('Bad', 'Ruim'),
    ('Beautiful', 'Bonito'),
    ('Ugly', 'Feio'),
    ('Old', 'Velho'),
    ('Young', 'Jovem'),
    ('Rich', 'Rico'),
    ('Poor', 'Pobre'),
    ('Tall', 'Alto'),
    ('Short', 'Baixo'),
    ('Fast', 'Rápido'),
    ('Slow', 'Lento'),
    ('Hot', 'Quente'),
    ('Cold', 'Frio'),
    ('Bright', 'Brilhante'),
    ('Dark', 'Escuro'),
    ('Hard', 'Difícil'),
    ('Soft', 'Macio'),
    ('Heavy', 'Pesado'),
    ('Light', 'Leve'),
    ('Happy', 'Feliz'),
    ('Sad', 'Triste'),
    ('Exciting', 'Empolgante'),
    ('Boring', 'Chato'),
    ('Interesting', 'Interessante'),
    ('Bitter', 'Amargo'),
    ('Sweet', 'Doce'),
    ('Salty', 'Salgado'),
    ('Sour', 'Azedo'),
    ('Delicious', 'Delicioso'),
    ('Tasteless', 'Insosso'),
    ('Fragrant', 'Fragrante'),
    ('Odorless', 'Inodoro'),
    ('Noisy', 'Barulhento'),
    ('Quiet', 'Silencioso'),
    ('Loud', 'Alto'),
    ('Silent', 'Silencioso'),
    ('Dirty', 'Sujo'),
    ('Tidy', 'Arrumado'),
    ('Messy', 'Bagunçado'),
    ('Fresh', 'Fresco'),
    ('Stale', 'Velho'),
    ('Smooth', 'Suave'),
    ('Rough', 'Áspero'),
    ('Shiny', 'Brilhante'),
    ('Colorful', 'Colorido'),
    ('Vibrant', 'Vibrante'),
    ('Dazzling', 'Deslumbrante'),
    ('Extraordinary', 'Extraordinário'),
    ('Unique', 'Único'),
    ('Common', 'Comum'),
    ('Rare', 'Raro'),
    ('Polished', 'Polido'),
    ('Unpolished', 'Não polido'),
    ('Neat', 'Arrumado'),
    ('Sloppy', 'Desleixado'),
    ('Wet', 'Molhado'),
    ('Dry', 'Seco'),
    ('Tangled', 'Embaraçado'),
    ('Untangled', 'Desembaraçado'),
    ('Clean', 'Limpo'),
    ('Soiled', 'Sujado'),
    ('Wild', 'Selvagem'),
    ('Domesticated', 'Doméstico'),
    ('Fierce', 'Feroz'),
    ('Gentle', 'Gentil'),
    ('Cruel', 'Cruel'),
    ('Kind', 'Bondoso'),
    ('Friendly', 'Amigável'),
    ('Hostile', 'Hostil'),
    ('Generous', 'Generoso'),
    ('Stingy', 'Avarento'),
    ('Brave', 'Corajoso'),
    ('Cowardly', 'Covarde'),
    ('Strong', 'Forte'),
    ('Weak', 'Fraco'),
    ('Sharp', 'Afiado'),
    ('Blind', 'Cego'),
    ('Healthy', 'Saudável'),
    ('Unhealthy', 'Insalubre'),
    ('Thin', 'Fino'),
    ('Thick', 'Espesso'),
    ('Sensitive', 'Sensível'),
    ('Insensitive', 'Insensível'),
    ('Grumpy', 'Rabugento'),
    ('Positive', 'Positivo'),
    ('Negative', 'Negativo'),
    ('Polite', 'Educado')
]

objects_places = [
    ('House', 'Casa'),
    ('Car', 'Carro'),
    ('Food', 'Comida'),
    ('Water', 'Água'),
    ('Money', 'Dinheiro'),
    ('School', 'Escola'),
    ('Work', 'Trabalho'),
    ('City', 'Cidade'),
    ('Country', 'País'),
    ('Time', 'Tempo'),
    ('Book', 'Livro'),
    ('Phone', 'Telefone'),
    ('Computer', 'Computador'),
    ('Internet', 'Internet'),
    ('Email', 'E-mail'),
    ('Social Media', 'Mídia Social'),
    ('Text', 'Texto'),
    ('Call', 'Ligação'),
    ('Camera', 'Câmera'),
    ('Website', 'Site'),
    ('Office', 'Escritório'),
    ('Bank', 'Banco'),
    ('Restaurant', 'Restaurante'),
    ('Coffee', 'Café'),
    ('Tea', 'Chá'),
    ('Bedroom', 'Quarto'),
    ('Bathroom', 'Banheiro'),
    ('Kitchen', 'Cozinha'),
    ('Living room', 'Sala de estar'),
    ('Garden', 'Jardim'),
    ('Park', 'Parque'),
    ('Street', 'Rua'),
    ('Store', 'Loja'),
    ('Mall', 'Shopping'),
    ('Market', 'Mercado'),
    ('Grocery', 'Mercearia'),
    ('Airport', 'Aeroporto'),
    ('Train', 'Trem'),
    ('Bus', 'Ônibus'),
    ('Plane', 'Avião'),
    ('Desk', 'Mesa'),
    ('Chair', 'Cadeira'),
    ('Table', 'Mesa'),
    ('Lamp', 'Lâmpada'),
    ('Bed', 'Cama'),
    ('Clock', 'Relógio'),
    ('Watch', 'Relógio'),
    ('Wallet', 'Carteira'),
    ('Bag', 'Mochila'),
    ('Shoes', 'Sapatos'),
    ('Clothes', 'Roupas'),
    ('Hat', 'Chapéu'),
    ('Jacket', 'Jaqueta'),
    ('Sunglasses', 'Óculos de sol'),
    ('Umbrella', 'Guarda-chuva'),
    ('Key', 'Chave'),
    ('Map', 'Mapa'),
    ('Globe', 'Globo'),
    ('Pen', 'Caneta'),
    ('Pencil', 'Lápis'),
    ('Paper', 'Papel'),
    ('Notebook', 'Caderno'),
    ('Magazine', 'Revista'),
    ('Newspaper', 'Jornal'),
    ('Passport', 'Passaporte'),
    ('ID', 'Identidade'),
    ('Credit card', 'Cartão de crédito'),
    ('Ticket', 'Bilhete'),
    ('Receipt', 'Recibo'),
    ('Invoice', 'Fatura'),
    ('Menu', 'Cardápio'),
    ('Plate', 'Prato'),
    ('Glass', 'Copo'),
    ('Fork', 'Garfo'),
    ('Spoon', 'Colher'),
    ('Knife', 'Faca'),
    ('Bowl', 'Tigela'),
    ('Pan', 'Panela'),
    ('Pot', 'Pote'),
    ('Oven', 'Forno'),
    ('Fridge', 'Geladeira'),
    ('Freezer', 'Freezer'),
    ('Microwave', 'Micro-ondas'),
    ('Television', 'Televisão'),
    ('Remote', 'Controle remoto'),
    ('Charger', 'Carregador'),
    ('Battery', 'Bateria'),
    ('Headphones', 'Fones de ouvido'),
    ('Toothbrush', 'Escova de dente'),
    ('Toothpaste', 'Pasta de dente'),
    ('Soap', 'Sabonete'),
    ('Towel', 'Toalha'),
    ('Toilet', 'Vaso sanitário'),
    ('Sink', 'Pia')
]

nature_weather = [
    ('Sun', 'Sol'),
    ('Moon', 'Lua'),
    ('Sky', 'Céu'),
    ('Cloud', 'Nuvem'),
    ('Rain', 'Chuva'),
    ('Wind', 'Vento'),
    ('Snow', 'Neve'),
    ('Storm', 'Tempestade'),
    ('Thunder', 'Trovão'),
    ('Lightning', 'Relâmpago'),
    ('Rainbow', 'Arco-íris'),
    ('Fog', 'Neblina'),
    ('Mist', 'Névoa'),
    ('Ice', 'Gelo'),
    ('Frost', 'Geada'),
    ('Breeze', 'Brisa'),
    ('Tornado', 'Tornado'),
    ('Hurricane', 'Furacão'),
    ('Tsunami', 'Tsunami'),
    ('Earthquake', 'Terremoto'),
    ('Volcano', 'Vulcão'),
    ('Mountain', 'Montanha'),
    ('Hill', 'Colina'),
    ('Valley', 'Vale'),
    ('River', 'Rio'),
    ('Lake', 'Lago'),
    ('Pond', 'Lagoa'),
    ('Stream', 'Riacho'),
    ('Ocean', 'Oceano'),
    ('Sea', 'Mar'),
    ('Beach', 'Praia'),
    ('Sand', 'Areia'),
    ('Rock', 'Pedra'),
    ('Pebble', 'Seixo'),
    ('Forest', 'Floresta'),
    ('Tree', 'Árvore'),
    ('Plant', 'Planta'),
    ('Flower', 'Flor'),
    ('Grass', 'Grama'),
    ('Bush', 'Arbusto'),
    ('Leaf', 'Folha'),
    ('Branch', 'Ramo'),
    ('Trunk', 'Tronco'),
    ('Root', 'Raiz'),
    ('Soil', 'Solo'),
    ('Mud', 'Lama'),
    ('Desert', 'Deserto'),
    ('Oasis', 'Oásis'),
    ('Canyon', 'Cânion'),
    ('Glacier', 'Glaciar'),
    ('Erosion', 'Erosão'),
    ('Drought', 'Seca'),
    ('Flood', 'Enchente'),
    ('Avalanche', 'Avalanche'),
    ('Sunrise', 'Amanhecer'),
    ('Sunset', 'Entardecer'),
    ('Day', 'Dia'),
    ('Night', 'Noite'),
    ('Morning', 'Manhã'),
    ('Afternoon', 'Tarde'),
    ('Evening', 'Noite'),
    ('Seasons', 'Estações'),
    ('Spring', 'Primavera'),
    ('Summer', 'Verão'),
    ('Autumn/Fall', 'Outono'),
    ('Winter', 'Inverno'),
    ('Heat', 'Calor'),
    ('Cold', 'Frio'),
    ('Temperature', 'Temperatura'),
    ('Humidity', 'Umidade'),
    ('Dew', 'Orvalho'),
    ('Frostbite', 'Congelamento'),
    ('Sleet', 'Granizo'),
    ('Drizzle', 'Garoa'),
    ('Heatwave', 'Onda de calor'),
    ('Blizzard', 'Nevasca'),
    ('Smog', 'Poluição atmosférica'),
    ('Pollen', 'Pólen'),
    ('Meteor', 'Meteoro'),
    ('Comet', 'Cometa'),
    ('Star', 'Estrela'),
    ('Planet', 'Planeta'),
    ('Galaxy', 'Galáxia'),
    ('Constellation', 'Constelação'),
    ('Eclipse', 'Eclipse'),
    ('Aurora', 'Aurora'),
    ('Climate', 'Clima'),
    ('Weather forecast', 'Previsão do tempo'),
    ('Natural disaster', 'Desastre natural'),
    ('Ecosystem', 'Ecossistema'),
    ('Conservation', 'Conservação'),
    ('Wildlife', 'Vida selvagem'),
    ('Habitat', 'Habitat'),
    ('Endangered species', 'Espécies ameaçadas'),
    ('Biodiversity', 'Biodiversidade'),
    ('Greenhouse effect', 'Efeito estufa')
]

health_body = [
    ('Health', 'Saúde'),
    ('Body', 'Corpo'),
    ('Mind', 'Mente'),
    ('Exercise', 'Exercício'),
    ('Nutrition', 'Nutrição'),
    ('Diet', 'Dieta'),
    ('Weight', 'Peso'),
    ('Fitness', 'Fitness'),
    ('Wellness', 'Bem-estar'),
    ('Healthy', 'Saudável'),
    ('Doctor', 'Médico'),
    ('Nurse', 'Enfermeiro'),
    ('Hospital', 'Hospital'),
    ('Clinic', 'Clínica'),
    ('Medicine', 'Medicamento'),
    ('Treatment', 'Tratamento'),
    ('Therapy', 'Terapia'),
    ('Vaccination', 'Vacinação'),
    ('Pain', 'Dor'),
    ('Injury', 'Lesão'),
    ('Recovery', 'Recuperação'),
    ('Checkup', 'Checagem'),
    ('Diagnosis', 'Diagnóstico'),
    ('Symptoms', 'Sintomas'),
    ('Prescription', 'Prescrição'),
    ('Allergy', 'Alergia'),
    ('Asthma', 'Asma'),
    ('Diabetes', 'Diabetes'),
    ('High Blood Pressure', 'Pressão Alta'),
    ('Low Blood Pressure', 'Pressão Baixa'),
    ('Heart', 'Coração'),
    ('Lungs', 'Pulmões'),
    ('Brain', 'Cérebro'),
    ('Bones', 'Ossos'),
    ('Muscles', 'Músculos'),
    ('Skin', 'Pele'),
    ('Eyes', 'Olhos'),
    ('Ears', 'Ouvidos'),
    ('Mouth', 'Boca'),
    ('Teeth', 'Dentes'),
    ('Stomach', 'Estômago'),
    ('Intestines', 'Intestinos'),
    ('Liver', 'Fígado'),
    ('Kidneys', 'Rins'),
    ('Bladder', 'Bexiga'),
    ('Immune System', 'Sistema Imunológico'),
    ('Digestive System', 'Sistema Digestivo'),
    ('Respiratory System', 'Sistema Respiratório'),
    ('Circulatory System', 'Sistema Circulatório'),
    ('Nervous System', 'Sistema Nervoso'),
    ('Hormones', 'Hormônios'),
    ('Mental Health', 'Saúde Mental'),
    ('Physical Health', 'Saúde Física'),
    ('Fitness Level', 'Nível de Fitness'),
    ('Healthy Eating', 'Alimentação Saudável'),
    ('Balanced Diet', 'Dieta Balanceada'),
    ('Hydration', 'Hidratação'),
    ('Sleep', 'Sono'),
    ('Rest', 'Descanso'),
    ('Stress', 'Estresse'),
    ('Anxiety', 'Ansiedade'),
    ('Depression', 'Depressão'),
    ('Relaxation', 'Relaxamento'),
    ('Meditation', 'Meditação'),
    ('Yoga', 'Ioga'),
    ('Pilates', 'Pilates'),
    ('Cardio', 'Cardio'),
    ('Flexibility', 'Flexibilidade'),
    ('Endurance', 'Resistência'),
    ('Agility', 'Agilidade'),
    ('Massage', 'Massagem'),
    ('Chiropractic', 'Quiropraxia'),
    ('Acupuncture', 'Acupuntura'),
    ('Herbal Medicine', 'Medicina Natural'),
    ('Homeopathy', 'Homeopatia'),
    ('Alternative Medicine', 'Medicina Alternativa'),
    ('Physiotherapy', 'Fisioterapia'),
    ('Occupational Therapy', 'Terapia Ocupacional'),
    ('Dietary Supplements', 'Suplementos Alimentares'),
    ('Healthy Habits', 'Hábitos Saudáveis'),
    ('Preventive Care', 'Cuidados Preventivos'),
    ('First Aid', 'Primeiros Socorros'),
    ('Hygiene', 'Higiene'),
    ('Cleanliness', 'Limpeza'),
    ('Sanitation', 'Saneamento'),
    ('Personal Hygiene', 'Higiene Pessoal'),
    ('Hand Washing', 'Lavagem das mãos'),
    ('Oral Hygiene', 'Higiene bucal'),
    ('Health Monitoring', 'Monitoramento de Saúde'),
    ('Mental Health Support', 'Apoio à Saúde Mental'),
    ('Healthy Lifestyle', 'Estilo de Vida Saudável'),
    ('Physical Activity', 'Atividade Física'),
    ('Health Awareness', 'Conscientização da Saúde'),
    ('Health Education', 'Educação em Saúde'),
    ('Rehabilitation', 'Reabilitação'),
    ('Recovery Process', 'Processo de Recuperação'),
    ('Health Maintenance', 'Manutenção da Saúde')
]

education_learning = [
    ('Education', 'Educação'),
    ('Learning', 'Aprendizado'),
    ('School', 'Escola'),
    ('Teacher', 'Professor'),
    ('Student', 'Aluno'),
    ('Classroom', 'Sala de aula'),
    ('Lesson', 'Aula'),
    ('Study', 'Estudo'),
    ('Knowledge', 'Conhecimento'),
    ('Books', 'Livros'),
    ('Library', 'Biblioteca'),
    ('Reading', 'Leitura'),
    ('Writing', 'Escrita'),
    ('Arithmetic', 'Aritmética'),
    ('Mathematics', 'Matemática'),
    ('Science', 'Ciência'),
    ('Biology', 'Biologia'),
    ('Chemistry', 'Química'),
    ('Physics', 'Física'),
    ('History', 'História'),
    ('Geography', 'Geografia'),
    ('Language', 'Idioma'),
    ('Literature', 'Literatura'),
    ('Grammar', 'Gramática'),
    ('Vocabulary', 'Vocabulário'),
    ('Homework', 'Tarefa de casa'),
    ('Test', 'Prova'),
    ('Exam', 'Exame'),
    ('Grade', 'Nota'),
    ('Report Card', 'Boletim Escolar'),
    ('Diploma', 'Diploma'),
    ("Bachelor's Degree", 'Graduação'),
    ("Master's Degree", 'Mestrado'),
    ('Doctorate/Ph.D.', 'Doutorado'),
    ('Online Learning', 'Aprendizado online'),
    ('Virtual Classroom', 'Sala de aula virtual'),
    ('Distance Education', 'Educação a distância'),
    ('School Supplies', 'Materiais escolares'),
    ('Backpack', 'Mochila'),
    ('Notebook', 'Caderno'),
    ('Pen', 'Caneta'),
    ('Pencil', 'Lápis'),
    ('Eraser', 'Borracha'),
    ('Sharpener', 'Apontador'),
    ('Ruler', 'Régua'),
    ('Calculator', 'Calculadora'),
    ('Project', 'Projeto'),
    ('Assignment', 'Tarefa'),
    ('Presentation', 'Apresentação'),
    ('Group Work', 'Trabalho em grupo'),
    ('Collaboration', 'Colaboração'),
    ('Research', 'Pesquisa'),
    ('Study Group', 'Grupo de estudo'),
    ('Educational Technology', 'Tecnologia educacional'),
    ('Interactive Whiteboard', 'Quadro interativo'),
    ('Lectures', 'Palestras'),
    ('Seminars', 'Seminários'),
    ('Workshops', 'Oficinas'),
    ('Curriculum', 'Currículo'),
    ('Pedagogy', 'Pedagogia'),
    ('Teaching Methods', 'Métodos de ensino'),
    ('Classroom Management', 'Gestão de sala de aula'),
    ('Educational Psychology', 'Psicologia educacional'),
    ('Special Education', 'Educação especial'),
    ('Inclusive Education', 'Educação inclusiva'),
    ('Literacy', 'Alfabetização'),
    ('Critical Thinking', 'Pensamento crítico'),
    ('Problem-Solving', 'Resolução de problemas'),
    ('Creativity', 'Criatividade'),
    ('Innovation', 'Inovação'),
    ('Adaptability', 'Adaptabilidade'),
    ('Skill', 'Habilidade'),
    ('Motivation', 'Motivação'),
    ('Engagement', 'Engajamento'),
    ('Assessment', 'Avaliação'),
    ('Grading System', 'Sistema de avaliação'),
    ('Continuous Learning', 'Aprendizado contínuo'),
    ('Interactive Learning', 'Aprendizado interativo'),
    ('Academic Achievement', 'Realização acadêmica'),
    ('Educational Resources', 'Recursos educacionais'),
    ('Educational Policy', 'Política educacional'),
    ('Educational Equity', 'Equidade educacional'),
    ('Classroom Environment', 'Ambiente escolar'),
    ('Educational Leadership', 'Liderança educacional'),
    ('Educational Assessment', 'Avaliação educacional'),
    ('School Administration', 'Administração escolar'),
    ('Educational Research', 'Pesquisa educacional')
]

work_careers = [
    ('Work', 'Trabalho'),
    ('Career', 'Carreira'),
    ('Job', 'Emprego'),
    ('Employment', 'Emprego'),
    ('Profession', 'Profissão'),
    ('Occupation', 'Ocupação'),
    ('Employee', 'Empregado'),
    ('Employer', 'Empregador'),
    ('Workplace', 'Local de trabalho'),
    ('Office', 'Escritório'),
    ('Company', 'Empresa'),
    ('Corporation', 'Corporação'),
    ('Business', 'Negócio'),
    ('Entrepreneurship', 'Empreendedorismo'),
    ('Self-employed', 'Autônomo'),
    ('Part-time', 'Meio período'),
    ('Full-time', 'Tempo integral'),
    ('Contract', 'Contrato'),
    ('Salary', 'Salário'),
    ('Wages', 'Salário'),
    ('Income', 'Renda'),
    ('Paycheck', 'Contracheque'),
    ('Benefits', 'Benefícios'),
    ('Promotion', 'Promoção'),
    ('Raise', 'Aumento de salário'),
    ('Interview', 'Entrevista'),
    ('Resume/CV', 'Currículo'),
    ('Cover Letter', 'Carta de apresentação'),
    ('Skills', 'Habilidades'),
    ('Qualifications', 'Qualificações'),
    ('Experience', 'Experiência'),
    ('Training', 'Treinamento'),
    ('Internship', 'Estágio'),
    ('Apprenticeship', 'Aprendizado'),
    ('Remote Work', 'Trabalho remoto'),
    ('Telecommuting', 'Teletrabalho'),
    ('Flexible Hours', 'Horário flexível'),
    ('Deadline', 'Prazo'),
    ('Task', 'Tarefa'),
    ('Project', 'Projeto'),
    ('Meeting', 'Reunião'),
    ('Collaboration', 'Colaboração'),
    ('Teamwork', 'Trabalho em equipe'),
    ('Leadership', 'Liderança'),
    ('Management', 'Gerenciamento'),
    ('Colleague', 'Colega de trabalho'),
    ('Mentor', 'Mentor'),
    ('Burnout', 'Esgotamento'),
    ('Stress', 'Estresse'),
    ('Productivity', 'Produtividade'),
    ('Efficiency', 'Eficiência'),
    ('Initiative', 'Iniciativa'),
    ('Innovation', 'Inovação'),
    ('Creativity', 'Criatividade'),
    ('Adaptability', 'Adaptabilidade'),
    ('Problem-solving', 'Resolução de problemas'),
    ('Decision-making', 'Tomada de decisão'),
    ('Communication', 'Comunicação'),
    ('Conflict Resolution', 'Resolução de conflitos'),
    ('Time Management', 'Gerenciamento do tempo'),
    ('Professionalism', 'Profissionalismo'),
    ('Ethics', 'Ética'),
    ('Work Environment', 'Ambiente de trabalho'),
    ('Workplace Culture', 'Cultura do local de trabalho'),
    ('Diversity', 'Diversidade'),
    ('Inclusion', 'Inclusão'),
    ('Equity', 'Equidade'),
    ('Career Growth', 'Crescimento profissional'),
    ('Advancement', 'Avanço'),
    ('Job Satisfaction', 'Satisfação no trabalho'),
    ('Retirement', 'Aposentadoria'),
    ('Resignation', 'Resignação'),
    ('Termination', 'Demissão'),
    ('Layoff', 'Demissão em massa'),
    ('Unemployment', 'Desemprego'),
    ('Job Market', 'Mercado de trabalho'),
    ('Job Search', 'Busca por emprego'),
    ('Employment Agency', 'Agência de empregos'),
    ('Human Resources', 'Recursos humanos'),
    ('Hiring', 'Contratação'),
    ('Firing', 'Demissão'),
    ('Redundancy', 'Redundância'),
    ('Job Posting', 'Anúncio de emprego'),
    ('Career Fair', 'Feira de carreiras'),
    ('Professional Networking', 'Networking profissional'),
    ('Career Path', 'Caminho da carreira'),
    ('Professional Goals', 'Objetivo profissionais'),
    ('Work Ethic', 'Ética de trabalho'),
    ('Remote Collaboration', 'Colaboração remota'),
    ('Workplace Safety', 'Segurança no trabalho'),
    ('Job Security', 'Segurança no emprego')
]

technology_communication = [
    ('Computer', 'Computador'),
    ('Smartphone', 'Celular'),
    ('Tablet', 'Tablet'),
    ('Desktop', 'Computador'),
    ('Screen', 'Tela'),
    ('Keyboard', 'Teclado'),
    ('Mouse', 'Mouse'),
    ('Printer', 'Impressora'),
    ('Charger', 'Carregador'),
    ('Cable', 'Cabo'),
    ('Battery', 'Bateria'),
    ('App', 'Aplicativo'),
    ('Operating System', 'Sistema Operacional'),
    ('Social Media', 'Mídias Sociais'),
    ('Website', 'Site'),
    ('Search Engine', 'Motor de busca'),
    ('Browser', 'Navegador'),
    ('Cloud', 'Nuvem'),
    ('Data', 'Dados'),
    ('Storage', 'Armazenamento'),
    ('File', 'Arquivo'),
    ('Folder', 'Pasta'),
    ('Memory', 'Memória'),
    ('Hard Drive', 'Disco rígido'),
    ('Speaker', 'Alto-falante'),
    ('Microphone', 'Microfone'),
    ('Headphones', 'Fones de ouvido'),
    ('Virtual Reality', 'Realidade virtual'),
    ('Artificial Intelligence', 'Inteligência Artificial'),
    ('Automation', 'Automação'),
    ('Robotics', 'Robótica'),
    ('Satellite', 'Satélite'),
    ('Network', 'Rede'),
    ('Connectivity', 'Conectividade'),
    ('Encryption', 'Criptografia'),
    ('Password', 'Senha'),
    ('Username', 'Nome de usuário'),
    ('Privacy', 'Privacidade'),
    ('Gaming', 'Jogos'),
    ('Social Networking', 'Rede social'),
    ('Text Message', 'Mensagem de texto'),
    ('Video Conference', 'Videoconferência'),
    ('Notification', 'Notificação'),
    ('Update', 'Atualização'),
    ('Upgrade', 'Atualizar'),
    ('Online Payment', 'Pagamento online'),
    ('Remote', 'Remoto'),
    ('Telecommuting', 'Teletrabalho'),
    ('Password Protection', 'Proteção de senha'),
    ('Tech Support', 'Suporte técnico'),
    ('Software Update', 'Atualização de software'),
    ('User Interface', 'Interface do usuário'),
    ('Data Security', 'Segurança de dados'),
    ('Digitalization', 'Digitalização')
]


# Função para criar a tabela e inserir as palavras
def criar_bd():
    conn = conectar_bd()
    cursor = conn.cursor()

    # Criar tabela se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actions_activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emotions_feelings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS family_relationship (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS descriptive_words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS objects_places (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nature_weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS health_body (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS education_learning (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS work_careers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS technology_communication (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_english VARCHAR(25) NOT NULL UNIQUE,
            word_portuguese VARCHAR(25) NOT NULL
        )
    ''')

    # Inserir as palavras na tabela
    cursor.executemany("INSERT INTO actions_activities (word_english, word_portuguese) VALUES (?, ?)", actions_activities)

    cursor.executemany("INSERT INTO emotions_feelings (word_english, word_portuguese) VALUES (?, ?)", emotions_feelings)

    cursor.executemany("INSERT INTO family_relationship (word_english, word_portuguese) VALUES (?, ?)", family_relationship)

    cursor.executemany("INSERT INTO descriptive_words (word_english, word_portuguese) VALUES (?, ?)", descriptive_words)

    cursor.executemany("INSERT INTO objects_places (word_english, word_portuguese) VALUES (?, ?)", objects_places)

    cursor.executemany("INSERT INTO nature_weather (word_english, word_portuguese) VALUES (?, ?)", nature_weather)

    cursor.executemany("INSERT INTO health_body (word_english, word_portuguese) VALUES (?, ?)", health_body)

    cursor.executemany("INSERT INTO education_learning (word_english, word_portuguese) VALUES (?, ?)", education_learning)

    cursor.executemany("INSERT INTO work_careers (word_english, word_portuguese) VALUES (?, ?)", work_careers)

    cursor.executemany("INSERT INTO technology_communication (word_english, word_portuguese) VALUES (?, ?)", technology_communication)


    # Commit e fechar a conexão
    conn.commit()
    conn.close()

if __name__ == '__main__':
    criar_bd()
