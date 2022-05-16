from configparser import ConfigParser
import pathlib
# reads and print the ini File
def print_my_ini(ini):
    config = ConfigParser()
    print(config.read(ini))
    print(ini)
    print()
    print ("Sections              : ", config.sections())
    print()
    print("DataTypes")
    print ("test_string      : ", config.get('DataTypes','test_string'))
    print ("test_int         : ", config.getint('DataTypes','test_int'))
    print ("test_float       : ", config.getfloat('DataTypes', 'test_float'))
    print ("test_bool_a      : ", config.getboolean('DataTypes', 'test_bool_a'))
    print ("test_bool_b      : ", config.getboolean('DataTypes', 'test_bool_b'))
    print ("test_bool_c      : ", config.getboolean('DataTypes', 'test_bool_c'))
    print ("test_bool_d      : ", config.getboolean('DataTypes', 'test_bool_d'))
    print()
    print("Concat_strings")
    print ("home_dir         : ", config.get('Concat_strings','home_dir'))
    print ("my_dir           : ", config.get('Concat_strings','my_dir'))
    print ("my_lib           : ", config.get('Concat_strings','my_lib'))
    print()
    print("namespace")
    print("space in key test : ", config.get('namespace','space in key test'))
    print()
    print("Escape")
    print ("Percentage       : ", config.get('Escape','Percentage'))

def change_my_ini(old_ini, new_ini):#
    config = ConfigParser()
    print(config.read(old_ini))
    
    new_test_string = "now changed"
    new_test_int = 5
    new_test_float = 5.5
    test_bool_true = True
    test_bool_false = False
    test_percentage = "50%%"


    #change entries
    config.set('DataTypes','test_string', new_test_string)
    config.set('DataTypes','test_int', str(new_test_int))
    config.set('DataTypes','test_float', str(new_test_float))
    config.set('DataTypes','test_bool_a', str(test_bool_true))
    config.set('DataTypes','test_bool_b', str(test_bool_true))
    config.set('DataTypes','test_bool_c', str(test_bool_false))
    config.set('DataTypes','test_bool_d', str(test_bool_false))
    config.set('Escape','Percentage', test_percentage)

    #save changes
    with open(new_ini, 'w') as configfile:
        config.write(configfile)



absolut_script_directory = pathlib.Path(__file__).parent.absolute()
old_ini_name = "example_config.ini"
new_ini_name = "config.ini"

abolute_ini_path = "{}{}{}".format(absolut_script_directory,"\\",old_ini_name)
absolute_ini_path_new = "{}{}{}".format(absolut_script_directory,"\\",new_ini_name)


print_my_ini(abolute_ini_path)
print()
print()
change_my_ini(abolute_ini_path, absolute_ini_path_new)
print()
print()
print_my_ini(absolute_ini_path_new)