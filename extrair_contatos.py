from telethon.sync import TelegramClient

# Substitua pelos seus dados
API_ID = "*"
API_HASH = "*"
PHONE_NUMBER = "*"  # Exemplo: +5511999999999
GROUP_NAME = "*"  # Nome exato do grupo

with TelegramClient('session', API_ID, API_HASH) as client:
    # Lista todos os grupos que você participa
    for dialog in client.iter_dialogs():
        if dialog.title == GROUP_NAME:
            group = dialog.entity
            break
    else:
        print("Grupo não encontrado!")
        exit()

    participants = client.get_participants(group)

    # Salvar contatos em CSV
    with open("contatos_telegram.csv", "w", encoding="utf-8") as f:
        f.write("ID,Username,Nome,Telefone\n")
        for user in participants:
            user_id = user.id
            username = user.username if user.username else ""
            first_name = user.first_name if user.first_name else ""
            last_name = user.last_name if user.last_name else ""
            phone = user.phone if user.phone else ""

            f.write(f"{user_id},{username},{first_name} {last_name},{phone}\n")

    print("Contatos extraídos com sucesso! Arquivo salvo como contatos_telegram.csv")
