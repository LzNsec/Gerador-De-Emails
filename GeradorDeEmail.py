import random
import string

def generate_email(base, domain):
    username = base + ''.join(random.choice(string.ascii_lowercase) for _ in range(4))
    return f"{username}@{domain}"

def generate_random_email(domain):
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    return f"{username}@{domain}"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'example.com']

    print("Domínios disponíveis:")
    for idx, domain in enumerate(domains, start=1):
        print(f"{idx}. {domain}")

    selected_domain_idx = int(input("Selecione o número correspondente ao domínio de email desejado: "))
    while selected_domain_idx < 1 or selected_domain_idx > len(domains):
        print("Seleção inválida. Escolha um número válido.")
        selected_domain_idx = int(input("Selecione o número correspondente ao domínio de email desejado: "))
    
    selected_domain = domains[selected_domain_idx - 1]

    use_base_email = input("Deseja usar uma base para o email? (s/n): ").lower()
    if use_base_email == 's':
        base_email = input("Digite a base para o email (ex: nome.sobrenome): ")
        email_generator = lambda: generate_email(base_email, selected_domain)
    else:
        email_generator = lambda: generate_random_email(selected_domain)

    print("\nQuantidade de contas a serem geradas (1 a 5):")
    for i in range(1, 6):
        print(f"{i}. {i}")

    num_accounts = int(input("Selecione o número correspondente à quantidade de contas desejada: "))
    while num_accounts < 1 or num_accounts > 5:
        print("Quantidade inválida. Escolha um número entre 1 e 5.")
        num_accounts = int(input("Selecione o número correspondente à quantidade de contas desejada: "))

    password_length = int(input("Comprimento das senhas (mínimo 8): "))
    while password_length < 8:
        print("Comprimento inválido. A senha deve ter pelo menos 8 caracteres.")
        password_length = int(input("Comprimento das senhas (mínimo 8): "))

    print("\nContas geradas:")

    for _ in range(num_accounts):
        email = email_generator()
        password = generate_password(password_length)
        print(f"Email: {email}\nSenha: {password}\n")

if __name__ == "__main__":
    main()
