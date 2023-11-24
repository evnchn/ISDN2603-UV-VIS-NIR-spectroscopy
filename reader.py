import_string = \
'''
import sys
import numpy as np # numpy
import matplotlib.pyplot as plt # matplotlib
import matplotlib.colors as mcolors # matplotlib
import colorpy
'''

### LINK START! (https://github.com/evnchn/linkstart.py)
for line in import_string.splitlines():
    if "import" in line:
        # print(line) custom behaviour
        try:
            exec(line)
        except:
            if "#" in line:
                package_name = line.split("#")[-1]
            else:
                splits = line.split("import")
                if "from" in line:
                    package_name = splits[0].replace("from","")
                else:
                    package_name = splits[1]
            package_name = package_name.strip()
            print("Installing {}...".format(package_name))    
            import subprocess
            import sys
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            try:
                exec(line)
            except:
                print("Failed to install {}".format(package_name))
### DONE


import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import colormodels
import ciexyz

colormodels.init()
ciexyz.init()

color_array = np.array([list(colormodels.irgb_from_xyz(ciexyz.xyz_from_wavelength(x)) for x in range(360, 831))])

# Check alignment matplotlib
# color_array = np.array([list([255,255,255] for x in range(360, 831))])

print(color_array.shape)



def read_specimen_data(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.count(",") == 1:
                numbers = line.split(",")
                try:
                    numbers = [float(num) for num in numbers]
                    data.append(numbers)
                except ValueError:
                    pass

    return data

def plot_data(data, title="Specimen.dat"):
    # Generate a rainbow spectrum using HSV color space

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.plot(x, y)
    # plt.set_facecolor('black')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    ax = plt.gca()
    ax.set_facecolor('black')
    ax.set_xlim([min(x), max(x)])
    plt.imshow(color_array, extent=[360, 830, np.min(y), np.max(y)], aspect='auto', alpha=1)
    plt.axvline(x=400, color='r', linestyle='--')
    plt.axvline(x=700, color='r', linestyle='--')
    plt.show()

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print(f"Try {sys.argv[0]} [filename]")
    filename = input("Drag>").replace('"',"")

result = read_specimen_data(filename)

plot_data(result, filename)