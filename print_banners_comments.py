num_chars_array_pre = [120, 119, 100, 99, 90, 80,
                        79,  75,  72, 71, 70, 65, 60,
                        60,  50,  49, 40, 30, 25, 20,
                        15,  10,   5]

#num_chars_array = [ this_num for this_num in num_chars_array_pre \
#                      where this_num > 4 ]

num_chars_array = num_chars_array_pre

#custom_character = None
custom_character = "*"

for i in num_chars_array:
  print()
  print()
  print()
  print("@@@@@@@@@@@@@@@@@")
  print("@@             @@")
  print(f"@@@@ {i} @@@@")
  print("@@             @@")
  print("@@@@@@@@@@@@@@@@@")
  print()
  print()
  print("#" * i)
  print()
  print("-" * i)
  print()
  print("/" * i)
  print()
  print("+" * i)
  print()
  print("=" * i)
  print()
  print("_" * i)
  print()
  print(";" * i)
  print()
  print(":" * i)
  print()
  print("|" * i)
  print()
  print("'" * i)
  print()
  print('"' * i)
  print()
  if custom_character is not None:
    print(custom_character * i)
    print()
  ##endof:  if custom_character is not None
  
  if i > 6:
    print()
    print("<!--" + (i-7) * " " + "-->")
    print()
    print("<!--" + (i-7) * "-" + "-->")
    print()
    print("<!--" + (i-7) * "#" + "-->")
    print()
    print("<!--" + (i-7) * "+" + "-->")
    print()
    print("<!--" + (i-7) * "/" + "-->")
    print()
    print("<!--" + (i-7) * "|" + "-->")
    print()
    print("<!--" + (i-7) * "=" + "-->")
    print()
    print("<!--" + (i-7) * "<" + "-->")
    print()
    print("<!--" + (i-7) * ">" + "-->")
    print()
    if custom_character is not None:
      print("<!--" + (i-7) * custom_character + "-->")
      print()
    ##endof:  if custom_character is not None
  ##endof:  if i > 6
  
  if i > 8:
    print()
    print("<!--" + " " + (i-9) * "-" + " " + "-->")
    print()
    print("<!--" + " " + (i-9) * "#" + " " + "-->")
    print()
    print("<!--" + " " + (i-9) * "+" + " " + "-->")
    print()
    print("<!--" + " " + (i-9) * "/" + " " + "-->")
    print()
    print("<!--" + " " + (i-9) * "|" + " " + "-->")
    print()
    print("<!--" + " " + (i-9) * "=" + " " + "-->")
    print()
    print("<!--" + " " + (i-9) * "<" + " " + "-->")
    print()
    print("<!--" + " " + (i-9) * ">" + " " + "-->")
    print()
    if custom_character is not None:
      print("<!--" + " " + 
              (i-9) * custom_character + 
                " " + "-->")
      print()
    ##endof:  if custom_character is not None
  ##endof:  if i > 8
  
  print()
  print("/*" + (i-4) * " " + "*/")
  print()
  print("(*" + (i-4) * " " + "*)")
  print()
  print("/*" + (i-4) * "-" + "*/")
  print()
  print("(*" + (i-4) * "-" + "*)")
  print()
  print("/*" + (i-4) * "#" + "*/")
  print()
  print("(*" + (i-4) * "#" + "*)")
  print()
  print("/*" + (i-4) * "+" + "*/")
  print()
  print("(*" + (i-4) * "+" + "*)")
  print()
  print("/*" + (i-4) * "/" + "*/")
  print()
  print("(*" + (i-4) * "/" + "*)")
  print()
  print("/*" + (i-4) * "|" + "*/")
  print()
  print("(*" + (i-4) * "|" + "*)")
  print()
  print("/*" + (i-4) * "=" + "*/")
  print()
  print("(*" + (i-4) * "=" + "*)")
  print()
  if custom_character is not None:
    print("/*" + (i-4) * custom_character + "*/")
    print()
    print("(*" + (i-4) * custom_character + "*)")
    print()
  ##endof:  if custom_character is not None
  
  if i > 5:
    print()
    print("/*" + " " + (i-6) * "-" + " " + "*/")
    print()
    print("(*" + " " + (i-6) * "-" + " " + "*)")
    print()
    print("/*" + " " + (i-6) * "#" + " " + "*/")
    print()
    print("(*" + " " + (i-6) * "#" + " " + "*)")
    print()
    print("/*" + " " + (i-6) * "+" + " " + "*/")
    print()
    print("(*" + " " + (i-6) * "+" + " " + "*)")
    print()
    print("/*" + " " + (i-6) * "/" + " " + "*/")
    print()
    print("(*" + " " + (i-6) * "/" + " " + "*)")
    print()
    print("/*" + " " + (i-6) * "|" + " " + "*/")
    print()
    print("(*" + " " + (i-6) * "|" + " " + "*)")
    print()
    print("/*" + " " + (i-6) * "=" + " " + "*/")
    print()
    print("(*" + " " + (i-6) * "=" + " " + "*)")
    print()
    if custom_character is not None:
      print("/*" + " " +
              (i-6) * custom_character + 
                " " + "*/")
      print()
      print("(*" + " " +
              (i-6) * custom_character + 
                " " + "*)")
      print()
    ##endof:  if custom_character is not None
  ##endof:  if i > 5
  
  
  
  print()
  print("##" + (i-4) * " " + "##")
  print()
  print("#" + (i-1) * "-")
  print()
  print("##" + (i-2) * "-")
  print()
  print("##" + (i-4) * "-" + "##")
  print()
  print("#" + (i-1) * "+")
  print()
  print("##" + (i-2) * "+")
  print()
  print("##" + (i-4) * "+" + "##")
  print()
  print("#" + (i-1) * "=")
  print()
  print("##" + (i-2) * "=")
  print()
  print("##" + (i-4) * "=" + "##")
  print()
  print("#" + (i-1) * "/")
  print()
  print("##" + (i-2) * "/")
  print()
  print("##" + (i-4) * "/" + "##")
  print()
  print("#" + (i-1) * "|")
  print()
  print("##" + (i-2) * "|")
  print()
  print("##" + (i-4) * "|" + "##")
  print()
  if custom_character is not None:
    print("#" + (i-1) * custom_character)
    print()
    print("##" + (i-2) * custom_character)
    print()
    print("##" + (i-4) * custom_character + "##")
    print()
  ##endof:  if custom_character is not none
  
  
  print()
  print("//" + (i-4) * " " + "//")
  print()
  print("//" + (i-2) * "-")
  print()
  print("//" + (i-4) * "-" + "//")
  print()
  print("//" + (i-2) * "+")
  print()
  print("//" + (i-4) * "+" + "//")
  print()
  print("//" + (i-2) * "=")
  print()
  print("//" + (i-4) * "=" + "//")
  print()
  print("//" + (i-2) * "/")
  print()
  print("//" + (i-4) * "/" + "//")
  print()
  print("//" + (i-2) * "|")
  print()
  print("//" + (i-4) * "|" + "//")
  print()
  if custom_character is not None:
    print("//" + (i-2) * "-")
    print()
    print("//" + (i-4) * "-" + "//")
    print()
  ##endof:  if custom_character is not None
  
  print()
  print()
  print()
  
##endof:  for i in num_chars_array