import os


def main():
      i=0
      path="C:/Users/ADMIN/Desktop/VS/"
      for filename in os.listdir(path):
          my_dest = "img" + str(i) + ".jpg"
          my_sourse = path + filename
          my_dest = path + my_dest
          os.rename(my_sourse, my_dest)
          i += 1

if __name__ == '__main__':
    main()
