import os
import fileinput
import pathlib
import shutil
import sys
def main():
    cwd = os.getcwd()
    dir_list = os.listdir(cwd)
    
    print(dir_list)
    mats_created = []
    material_dir = cwd
    albedo_name = input("What is the suffix of your color texture? ")
    normal_name = input("What is the suffix of your normal texture? ")
    rough_name = input("What is the suffix of your roughness texture? ")
    metal_name = input("What is the suffix of your metal texture? ")
    alpha_name = input("What is the suffix of your alpha texture? ")
    if "_" not in albedo_name:
        albedo_name = "_" + albedo_name
    else:
        print("Proper format")
    if "_" not in normal_name:
        normal_name = "_" + normal_name
    else:
        print("Proper format")
    if "_" not in rough_name:
        rough_name = "_" + rough_name
    else:
        print("Proper format")
    if "_" not in metal_name:
        metal_name = "_" + metal_name
    if "_" not in alpha_name:
        alpha_name = "_" + alpha_name
    else:
        print("Proper format")
    
    vmats_to_be_created = []
    for i in dir_list:
        filename, file_extension = os.path.splitext(i)
        print(file_extension)
        print(filename)
        if file_extension != '.tga' and file_extension != '.png' and file_extension != '.jpg':
            print("Not an image file, continue")
        else:
            newmaterial = {
            "materialname": "",
            "albedo": "",
            "normal": "",
            "roughness": "",
            "metal": "",
            "alpha": ""
            }
            texnum = what_texture_is_it(filename, albedo_name, normal_name, rough_name, metal_name, alpha_name)
            if texnum == 1:                                             #If the texture is an albedo texture
                material_name = filename[:filename.find(albedo_name)]
                dictfound, booldict = checkfordict(material_name, vmats_to_be_created)
                if booldict == False:
                    newmaterial["materialname"] = material_name
                    newmaterial["albedo"] = material_dir + '\\' + filename + file_extension
                    vmats_to_be_created.append(newmaterial)
                    #print(vmats_to_be_created)
                else:
                    print("vmat dict is in system, filling in the texture")
                    temp = dictfound
                    temp["albedo"] = material_dir + '\\'  + filename + file_extension
                    print(temp)
            
            elif texnum == 2:
                material_name = filename[:filename.find(normal_name)]
                dictfound, booldict = checkfordict(material_name, vmats_to_be_created)
                if booldict == False:
                    newmaterial["materialname"] = material_name
                    newmaterial["albedo"] = material_dir + '\\' + filename + file_extension
                    vmats_to_be_created.append(newmaterial)
                    #print(vmats_to_be_created)
                else:
                    print("vmat dict is in system, filling in the texture")
                    temp = dictfound
                    temp["normal"] = material_dir + '\\' + filename + file_extension
            elif texnum == 3:
                material_name = filename[:filename.find(rough_name)]
                dictfound, booldict = checkfordict(material_name, vmats_to_be_created)
                if booldict == False:
                    newmaterial["materialname"] = material_name
                    newmaterial["roughness"] = material_dir + '\\' + filename + file_extension
                    vmats_to_be_created.append(newmaterial)
                    #print(vmats_to_be_created)
                else:
                    print("vmat dict is in system, filling in the texture")
                    temp = dictfound
                    temp["roughness"] = material_dir + '\\'  + filename + file_extension
            elif texnum == 4:
                material_name = filename[:filename.find(metal_name)]
                dictfound, booldict = checkfordict(material_name, vmats_to_be_created)
                if booldict == False:
                    newmaterial["materialname"] = material_name
                    newmaterial["metal"] = material_dir + '\\' + filename + file_extension
                    vmats_to_be_created.append(newmaterial)
                    #print(vmats_to_be_created)
            elif texnum == 5:
                material_name = filename[:filename.find(alpha_name)]
                dictfound, booldict = checkfordict(material_name, vmats_to_be_created)
                if booldict == False:
                    newmaterial["materialname"] = material_name
                    newmaterial["alpha"] = material_dir + '\\' + filename + file_extension
                    vmats_to_be_created.append(newmaterial)
                    #print(vmats_to_be_created)        
                else:
                    print("vmat dict is in system, filling in the texture")
                    temp = dictfound
                    temp["alpha"] = material_dir + '\\' + filename + file_extension        
            else:
                print("Error, no textures with that format name for that material")
    print(vmats_to_be_created)
    create_vmat(vmats_to_be_created)
            
        
        
        
def create_vmat(dict_list):
    for i in dict_list:
        print(i["albedo"])
        shutil.copy("examplevmat.vmat",i["materialname"]+".vmat")
        if i["albedo"] != "":
            for line in fileinput.input(i["materialname"]+".vmat", inplace = 1):
                    print(line.rstrip().replace('TextureColor "materials/default/default_color.tga"', 'TextureColor  "' + i["albedo"] + '"'))
        if i["metal"] != "":
            for line in fileinput.input(i["materialname"]+".vmat", inplace = 1): 
                    print(line.rstrip().replace('TextureMetalness "materials/default/default_metal.tga"', 'TextureMetalness "' + i["metal"]+ '"'))
        if i["normal"] != "":
            for line in fileinput.input(i["materialname"]+".vmat", inplace = 1): 
                    print(line.rstrip().replace('TextureNormal "materials/default/default_normal.tga"', 'TextureNormal "' + i["normal"]+ '"'))
        if i["roughness"] != "":
            for line in fileinput.input(i["materialname"]+".vmat", inplace = 1): 
                print(line.rstrip().replace('TextureRoughness "materials/default/default_rough.tga"', 'TextureRoughness "' + i["roughness"]+ '"'))
        if i["alpha"] != "":
            for line in fileinput.input(i["materialname"]+".vmat", inplace = 1): 
                print(line.rstrip().replace('TextureTranslucency "materials\dev\white_color.tga"', 'TextureTranslucency "' + i["alpha"]+ '"'))
            for line in fileinput.input(i["materialname"]+".vmat", inplace = 1):    
                print(line.rstrip().replace('F_ALPHA_TEST 0', 'F_ALPHA_TEST 1')) 
            for line in fileinput.input(i["materialname"]+".vmat", inplace = 1):    
                print(line.rstrip().replace('F_PREPASS_ALPHA_TEST 0', '	F_PREPASS_ALPHA_TEST 1')) 
    
    
        
    
def what_texture_is_it(filename, albedo_name, normal_name, rough_name, metal_name, alpha_name):
    if filename.find(albedo_name) != -1:
        return 1
    elif filename.find(normal_name) != -1:
        return 2
    elif filename.find(rough_name) != -1:
        return 3
    elif filename.find(metal_name) != -1:
        return 4
    elif filename.find(metal_name) != -1:
        return 4
    elif filename.find(alpha_name) != -1:
        return 5
    else:
        return -1
        
        
def checkfordict(mat_name, vmats_to_be_created):
    for i in vmats_to_be_created:
        print(i["materialname"])
        if i["materialname"] == mat_name:
            return i, True
        else:
            print("Not found yet! (checkfordict)")
    return {}, False
            
if __name__ == "__main__":
  main ()
