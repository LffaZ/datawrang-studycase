import os

def generate_env():
    env_file = '.env.example'
    new_env_file = '.env'
    
    # Cek apakah file .env sudah ada
    if os.path.exists(new_env_file):
        print(f"{new_env_file} already exists.")
        return
    
    # Membaca .env.example
    with open(env_file, 'r') as f:
        lines = f.readlines()
    
    # Buat file .env baru
    with open(new_env_file, 'w') as f:
        for line in lines:
            # Jika line kosong atau comment (dimulai dengan #), langsung tambahkan
            if line.strip() == '' or line.strip().startswith('#'):
                f.write(line)
            else:
                # Ambil nama variabel dari setiap baris
                key = line.split('=')[0]
                # Tanyakan ke user untuk mengisi nilai variabel
                value = input(f"Enter value for {key}: ")
                f.write(f"{key}={value}\n")
    
    print(f"{new_env_file} has been generated. Please check and update the values.")

if __name__ == "__main__":
    generate_env()
