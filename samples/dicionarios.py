import os
import platform


comandos_rename = {"Window": "rename {0} {1}",
                    "Linux": "mv {0} {1}",
                    "Darwin": "mv {0} {1}",
                    "Solaris" "renomear {0} {1}" }


# for value in comandos_rename.values():
#     print(value)
#     print("proximo")
#
def rename(nome_antigo, nome_novo):
    os.system(comandos[platform.system()].format(nome_antigo, nome_novo))


# def rename_not_portable(nome_antigo, nome_novo):
#     os.system("mv {} {}".format(nome_antigo, nome_novo))


rename_not_portable("novo.py", "antigo.py")
