import xml.etree.ElementTree as ET
from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
    
    tree = ET.parse('pom.xml')
    root = tree.getroot()

    for xml in root:
        if "groupId" in xml.tag:
            group = xml.tag
        if "artifactId" in xml.tag:
            artifact = xml.tag
        if "name" in xml.tag:
            name = xml.tag

    group_id = root.find(group)

    artifact_id = root.find(artifact)
    if "-" in artifact_id.text:
        artifact_id_text = artifact_id.text.replace("-", "")
    else:  
        artifact_id_text = artifact_id.text 

    project_name = root.find(name)
    project_name_text = project_name.text.replace("-", "").title()

    package = f"{group_id.text}.{artifact_id.text}"
    path_code_directory = f"src.main.java.{group_id.text}.{artifact_id_text}"
    path_test_code_directory = f"src.test.java.{group_id.text}.{artifact_id_text}"
    full_path_main_java_folder = path_code_directory.replace(".", "/")
    application_class_file_name = f"{project_name_text}Application.java"
    
    metadata.inputs['application_package'] = package
    metadata.inputs['application_package_folder'] = package.replace(".", "/")
    metadata.inputs['full_path_main_java_folder'] = path_code_directory.replace(".", "/")
    metadata.inputs['full_path_test_java_folder'] = path_test_code_directory.replace(".", "/")
    metadata.inputs['application_class_source_file_path'] = f"{full_path_main_java_folder}/{application_class_file_name}"

    return metadata