collections = {}
# Here we are creating a dictionary
def createCollection(p_collection_name):
    collections[p_collection_name] = []
    print(f"Collection '{p_collection_name}' created.")


# basic employee data set
employee_data = [
    {"EmployeeID": "E02001", "Name": "Karthik", "Department": "IT", "Gender": "Female"},
    {"EmployeeID": "E02002", "Name": "Charan", "Department": "HR", "Gender": "Male"},
    {"EmployeeID": "E02003", "Name": "Sravya", "Department": "IT", "Gender": "Female"}
]

# here we add employee data to the specified collection, excluding the provided column.
def indexData(p_collection_name, p_exclude_column):
    if p_collection_name in collections:
        for emp in employee_data:
            indexed_data = {k: v for k, v in emp.items() if k != p_exclude_column}
            collections[p_collection_name].append(indexed_data)
        print(f"Data indexed into collection '{p_collection_name}', excluding '{p_exclude_column}'")

# we search for employees in a collection where the specified column matches the provided value.
def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name in collections:
        results = [emp for emp in collections[p_collection_name] if emp.get(p_column_name) == p_column_value]
        print(f"Search results for '{p_column_name} = {p_column_value}' in collection '{p_collection_name}': {results}")

# This function will return the total number of employees in the specified collection.
def getEmpCount(p_collection_name):
    if p_collection_name in collections:
        emp_count = len(collections[p_collection_name])
        print(f"Employee count in collection '{p_collection_name}': {emp_count}")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")


# deleting an employee with their EmployeeID.
def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name in collections:
        collections[p_collection_name] = [emp for emp in collections[p_collection_name] if emp.get("EmployeeID") != p_employee_id]
        print(f"Employee with ID '{p_employee_id}' deleted from collection '{p_collection_name}'")

# we will count the number of employees grouped by department.
def getDepFacet(p_collection_name):
    if p_collection_name in collections:
        dep_count = {}
        for emp in collections[p_collection_name]:
            dep = emp.get("Department")
            if dep:
                dep_count[dep] = dep_count.get(dep, 0) + 1
        print(f"Department facet in collection '{p_collection_name}': {dep_count}")
        return dep_count

v_nameCollection = 'Hemachandra'
v_phoneCollection = '3286'
createCollection(v_nameCollection)
createCollection(v_phoneCollection)
getEmpCount(v_nameCollection)

indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

delEmpById(v_nameCollection, 'E02003')

getEmpCount(v_nameCollection)

searchByColumn(v_nameCollection, 'Department', 'IT')
searchByColumn(v_nameCollection, 'Gender', 'Male')

searchByColumn(v_phoneCollection, 'Department', 'IT')
getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)


