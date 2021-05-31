import os

while True:
	os.system("clear\n")
	os.system("tput setaf 1")
	print("\t LVM Automation")
	os.system("tput setaf 7")
	print("\t----------------")

	print("""
	Press 1: to check Total Disk
	Press 2: to create Physical Volume
	Press 3: to display Physical Volume
	Press 4: to create volume Group
	Press 5: to display Volume Group
	Press 6: to create Logical Volume
	Press 7: to display Logical Volume
	Press 8: to extend Size of Logical Volume
	Press 9: to Exit
	""")

	ch= input("Enter your choice:")
	if ch=="1":
		os.system("fdisk -l")

	elif ch=="2":
		n=input("Enter your Hard Disk name:")
		os.system(f"pvcreate {n}")
		print("PV created Successfully")
	elif ch=="3":
		n=input("Enter your Hard Disk name:")
		os.system(f"pvdisplay {n}")
	elif ch=="4":
		n=input("Enter the Name of your VG you want to create:")
		v=input("Enter your existing PV:")
		os.system(f"vgcreate {n} {v}")
		print("VG created Successfully")
	elif ch=="5":
		n=input("Enter your existing VG:")
		os.system(f"vgdisplay {n}")
	elif ch=="6":
		n=input("Enter the Name of your LV you want to create:")
		vg=input("Enter your existing VG name:")
		s=input("Enter this LV Volume Size:")
		os.system(f"lvcreate --size {s} --name {n} {vg}")		
		print("LV created Successfully")
		
		f=input("\nDo you want to Format this LV [y/n]:")
		if f=="y":
			os.system(f"mkfs.ext4 /dev/{vg}/{n}")
			print(f"{n} LV formated Successfully ")
		else:
			break
		
		m=input("\nDo you want to Mount this LV [y/n]:")
		if m=="y":
			c=input("\nDo you want to Create a new Directory & Mount [y/n]:")
			if c=="y":
				d=input("Enter Directory name you want to create:")
				os.system(f"mkdir /{d}")
				print(f"\nNew Directory named {d} created Successfully")
				os.system(f"mount /dev/{vg}/{n}  /{d}")
				print(f"LV named {n} mounted with {d} directory successfully")	
			else:
		
				d=input("Enter your existing Directory name:")
				os.system(f"mount /dev/{vg}/{n}  /{d}")
				print("LV named {n} mounted with {d} directory successfully")
	elif ch=="7":
		lv=input("Enter your existing LV name:")
		vg=input("Enter VG name of this LV:")
		os.system(f"lvdisplay {vg}/{lv}")
	elif ch=="8":
		lv=input("Enter your existing LV name:")
		vg=input("Enter VG name of this LV:")
		s=input("Enter the Size you want to Extend:")
		os.system(f"lvextend --size +{s} /dev/{vg}/{lv}")
		
		f=input("Press enter...")
		print("Reformating this LV...")
		os.system(f"resize2fs /dev/{vg}/{lv}")
		print("Your LV is Successfully extended")
	elif ch=="9":
		print("Thanks for using")
		break
	else:
		print("Please enter a valid option..")
	y=input("Press enter to continue...")
