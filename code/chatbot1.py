# CHATBOT Lionel 

# -----------------------------
# Funció que respon segons la pregunta de l'usuari
# -----------------------------
def respondre(pregunta, nom):
    # Passem la pregunta a minúscules per facilitar la comparació
    pregunta = pregunta.lower()

    # --- FUNCIONALITATS ESPECIALS ---
    if "pronostic" in pregunta or "resultat" in pregunta or "prediccio" in pregunta:
        # Només dóna pronòstic si és del Barça, Madrid o clàssic
        if ("barça" in pregunta) or ("madrid" in pregunta) or ("classic" in pregunta):
            return (
                f"El meu pronòstic per al pròxim clàssic és 2-1 pel Barça. "
                f"I tu, {nom}, quin resultat creus que hi haurà?"
            )
        else:
            return (
                f"De moment només puc fer pronòstics del clàssic Barça–Madrid, {nom}. "
                f"Vols que t’expliqui com veig aquest partit?"
            )

    elif "acudit" in pregunta or "broma" in pregunta:
        return (
            f"- Carinyo, estàs obsessionat amb el futbol i em fas falta.\n"
            f"- Què? Falta? Falta? Si ni tan sols t'he tocat!"
        )

    elif "millor" in pregunta or "compara" in pregunta:
        # Comprovem quins jugadors o equips es comparen
        if ("messi" in pregunta and "cristiano" in pregunta) or ("ronaldo" in pregunta and "messi" in pregunta):
            return (
                f"És difícil triar, {nom}. Messi té més visió de joc i creativitat, "
                f"mentre que Cristiano destaca pel seu físic i la seva mentalitat guanyadora."
            )
        elif "mbappé" in pregunta or "haaland" in pregunta:
            return (
                f"Mbappé és més ràpid i desequilibrant, {nom}, "
                f"mentre que Haaland és un golejador pur amb molta potència dins l’àrea."
            )
        elif "barça" in pregunta and "madrid" in pregunta:
            return (
                f"El Barça aposta més pel joc col·lectiu i de possessió,"
                f"mentre que el Madrid confia més en la intensitat i les transicions ràpides."
            )
        else:
            return (
                f"Depèn molt de què vulguis comparar, {nom}. "
                f"Parlem de jugadors, equips o estils de joc?"
            )

    # --- RESPOSTES NORMALS ---
    elif "hola" in pregunta:
        return (
            f"Hola, {nom}. Vols parlar d'algun equip o jugador? "
            f"Pots preguntar 'Parla'm del Barça' o 'Qui ha guanyat el Baló d'Or?'."
        )

    elif "com estàs" in pregunta or "què tal" in pregunta:
        return (
            f"Molt bé, {nom}. Preparat per parlar de futbol. "
            f"Pots preguntar 'Qui és Lamine Yamal?' o 'Qui va guanyar el Mundial?'."
        )

    elif "equip" in pregunta and "preferit" in pregunta:
        return (
            f"Jo sóc fan del Barça, {nom}. I tu? "
            f"Pots preguntar 'Parla'm del Barça' o 'Parla'm del Madrid'."
        )

    elif "barça" in pregunta or "barcelona" in pregunta:
        return (
            f"El Barça és un dels clubs més importants del món, {nom}. "
            f"Pots preguntar 'Qui és Lamine Yamal?'."
        )

    elif "madrid" in pregunta:
        return (
            f"El Real Madrid és un club amb moltes Champions, {nom}. "
            f"Pots preguntar 'Qui és Cristiano?' o 'Qui és Mbappé?'."
        )

    elif "messi" in pregunta:
        return (
            f"Messi és el millor jugador de la història, {nom}. "
            f"Pots preguntar 'Qui ha guanyat l'últim Baló d'Or?' o 'Parla'm de Cristiano'."
        )

    elif "cristiano" in pregunta or "ronaldo" in pregunta:
        return (
            f"Cristiano Ronaldo és una llegenda del futbol mundial, {nom}. Llàstima que no té cap mundial. "
            f"Pots preguntar 'On juga Haaland?' o 'Qui és el millor jugador actual?'."
        )

    elif "mbappé" in pregunta:
        return (
            f"Mbappé és una estrella francesa, molt ràpid i golejador, {nom}. "
            f"Pots preguntar 'On juga Mbappé ara?' o 'Parla'm de Haaland'."
        )

    elif "haaland" in pregunta:
        return (
            f"Haaland és un davanter noruec que juga al Manchester City, {nom}. "
            f"Pots preguntar 'Qui ha guanyat el Baló d'Or?' o 'Parla'm de Mbappé'."
        )

    elif "lamine" in pregunta or "yamal" in pregunta:
        return (
            f"Lamine Yamal és un jove jugador del Barça i de la selecció espanyola, {nom}. "
            f"Té molt talent i és un dels futbolistes més prometedors. "
            f"Pots preguntar 'Parla'm de Messi' o 'Qui ha guanyat el Baló d'Or?'."
        )

    elif "baló" in pregunta or "balon" in pregunta:
        return (
            f"L'últim Baló d'Or el va guanyar Ousmane Dembélé, {nom}, després d'una gran temporada. "
            f"Pots preguntar 'Parla'm de Mbappé' o 'Qui va guanyar el Mundial?'."
        )

    elif "mundial" in pregunta:
        return (
            f"L'últim Mundial el va guanyar l'Argentina el 2022, {nom}. "
            f"Pots preguntar 'Parla'm de Messi' o 'Qui ha guanyat el Baló d'Or?'."
        )

    elif "entrenador" in pregunta or "pep" in pregunta or "guardiola" in pregunta:
        return (
            f"Pep Guardiola és considerat un dels millors entrenadors del món, {nom}. "
            f"Actualment entrena el Manchester City. Pots preguntar 'Parla'm del Barça' o 'Què és la Champions?'."
        )

    elif "champions" in pregunta:
        return (
            f"La Champions és la competició més important d'Europa, {nom}. "
            f"L'última la va guanyar el Real Madrid. "
            f"Pots preguntar 'Parla'm del Madrid' o 'Qui és el millor jugador del món?'."
        )

    elif "millor jugador" in pregunta:
        return (
            f"És difícil escollir, {nom}, però molts pensen que Lamine i Dembélé estan actualment entre els millors. "
            f"Pots preguntar 'Parla'm de Messi' o 'Parla'm de Lamine Yamal'."
        )

    elif "adeu" in pregunta or "adéu" in pregunta:
        return f"Adéu, {nom}. Ha estat un plaer parlar amb tu de futbol."

    else:
        return (
            f"No estic segur d'això, {nom}. "
            f"Pots preguntar 'Parla'm del Barça', 'Qui és Lamine Yamal?' o 'Qui ha guanyat el Baló d'Or?'."
        )


# -----------------------------
# Funció que detecta i neteja el nom de l'usuari
# -----------------------------
def obtenir_nom(resposta_usuari):
    # Separem la frase en paraules individuals
    paraules = resposta_usuari.split()

    for paraula in paraules:
        # Busca la paraula en majúscula que podria ser el nom 
        if paraula[0].isupper():
            # Traiem possibles signes de puntuació del final
            nom = paraula.strip(",.!?")
            # Eliminem si el nom comença amb "l’", "l'", o "en"
            nom = nom.replace("l’", "").replace("l'", "").replace("en ", "").replace("En ", "")
            # Retornem el nom amb majúscula inicial
            return nom.capitalize()

    # Si no troba cap majúscula quan escriu l'usuari el nom, retorna l'inicial en majúscula 
    return resposta_usuari.strip().capitalize()


# -----------------------------
# Funció principal del programa
# -----------------------------
def main():
    print("⚽ Benvingut al Xatbot Lionel ⚽")
    print("Pots parlar amb mi de futbol. Si vols acabar la conversa, escriu 'adéu'.\n")

    resposta_nom = input("Abans de començar, com et dius? : ")
    nom = obtenir_nom(resposta_nom)

    print(f"\nEncantat de conèixer-te, {nom}.")
    print("Pots començar amb preguntes com:")
    print("- Parla'm del Barça")
    print("- Qui ha guanyat el Baló d'Or?")
    print("- Qui és Lamine Yamal?\n")

    while True:
        pregunta = input(f"{nom}: ")
        resposta = respondre(pregunta, nom)
        print("Bot:", resposta)

        if "adeu" in pregunta.lower() or "adéu" in pregunta.lower():
            break

# -----------------------------
# Executar el programa
# -----------------------------
if __name__ == "__main__":
    main()

