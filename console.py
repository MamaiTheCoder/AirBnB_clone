#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    def quit(self, line):
        """Close program and saves safely data."""
        return True

    def EOF(self, line):
        """Close program and saves safely data, when
        user input is CTRL + D.
        """
        print("")
        return True

    def help(self):
         """Prints help command description."""
         print("Provides description of a given command")

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def create(self, type_model):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")

    def show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')

        if args[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                 ob_name = value.__class__.__name__
                 ob_id = value.id
                 if ob_name == args[0] and ob_id == args[1].strip('"'):
                     del value
                     del storage._FileStorage__objects[key]
                     storage.save()
                     return
            print("** no instance found **")


    def all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        # prints the whole file
        storage.reload()
        my_json = []
        objects_dict = storage.all()
        if not arg:
            for key in objects_dict:
                my_json.append(str(objects_dict[key]))
                print(json.dumps(my_json))
                return
        token = shlex.split(arg)
        if token[0] in HBNBCommand.my_dict.keys():
            for key in objects_dict:
                if token[0] in key:
                    my_json.append(str(objects_dict[key]))
                    print(json.dumps(my_json))
                else:
                    print("** class doesn't exist **")

    def update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        a = ""
        
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                        return
            print("** no instance found **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
