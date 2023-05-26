from zipfile import ZipFile

# Extract zip file
def extract_zip_file(input_file: str, output_folder: str) -> int:
    """extract zip file

    Args:
        input_file (str): input file from which to extract
        output_file (str): output file in which to extract

    Returns:
        int: return 0 if successful
    """
    print(f"Extracting {input_file} file \n")
    with ZipFile(input_file, "r") as zObject:
        # Extracting all the members of the zip into a specific location.
        zObject.extractall(path=output_folder)
    print(f"Zip extracted. Output folder: {output_folder}")
    return 0


# zip file handler  
def list_zip_contents(zip_file:str):
    """List Zip files in the given Zip Archive

    Args:
        zip_file (str): zip file to get list of contents
    """
    zip = ZipFile('')

# list available files in the container
print(zip.namelist())


def main():
    zip_file = input('Enter zip file name: ')
    print(f'Zip file name: {zip_file}')
    list_zip_contents(zip_file=zip_file)
    
    extract_zip_file(input_file=zip_file, output_folder='repo')
    

if __name__=='__main__':
    main()