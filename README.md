# Python Batch VMAT Creator
##Requirements
-Python 3.11 or later
## Installation/Usage
1. Download the `batch_create_vmats.py` file and the `examplevmat.vmat` from this repository
2. Drop both into into a foler that's in your materials folder in your Half-Life Alyx addon's content folder (This is where your textures are and where the vmats will be created)
3. Make sure your textures are already prepared with proper suffix's denoting what type of texture it is (i.e. Color, Normal, Roughness, Metal, Alpha)
4. Run the python script in that folder and enter in the parameters accordingly, the materials path should be materials/your_folder, and the suffixes should match the ones you added to the texture names
5. The script should run for a little bit, depending on how many textures and materials you want to create it could take a couple of minutes
6. After the script is done, you can load into HLA and the materials should be in your material/asset browser and ready to use. It could freeze your HLA since the materials still need to be compiled
## Features to be added someday
- Add S&Box and CS2 support
- Support for other material types (idk why you'd need thousands of materials that aren't complex but its good to have)
- Automatic compiling after creating?
## Texture Suffix's
Texture suffix's are what are at the end of a texture file name to denote what tpye of texture it is. Weather it be a color map (_color, _alb, _c), normal map (_normal, _nrm, _n), roughness map (_rough, _rgh, _r), metal map (_metal, _mtl, _m), or alpha (_alpha, _alp, _a). You can chose whatever suffix you want for your textures, just make sure that they are the same for each type in the folder your creating vmats in.
