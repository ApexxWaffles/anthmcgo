import csv

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


def load_data(lst, csv_file, column_name):
    with open('insurance.csv') as csv_info:
        csv_dic = csv.DictReader(csv_info)
        for row in csv_dic: 
            lst.append(row[column_name])
    return lst


load_data(ages, 'insurance.csv', 'age')
load_data(sexes, 'insurance.csv', 'sex')
load_data(bmis, 'insurance.csv', 'bmi')
load_data(num_children, 'insurance.csv', 'children')
load_data(smoker_statuses, 'insurance.csv', 'smoker')
load_data(regions, 'insurance.csv', 'region')
load_data(insurance_charges, 'insurance.csv', 'charges')


class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, 
                 patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges


    def avarage_age(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        return f"Average Patient age: {round(total_age / len(self.patients_ages), 2)}"
        
    def sex_count(self):
        female = 0 
        male = 0 
        for sex in self.patients_sexes:
            if sex == 'female':
                female += 1
            elif sex == 'male':
                male += 1
        return f"Female: {female}\nMale: {male}"

    def bmi_average(self):
        bmi_total = 0
        for num in self.patients_bmis:
            bmi_total += float(num)
        return f"Average Patient BMI: {round(bmi_total / len(self.patients_bmis), 2)}"
        
    def difference_region(self):
        unique_regions = []
        for region in self.patients_regions:
            if region not in unique_regions:
                unique_regions.append(region)
        return unique_regions

    def average_cost(self):
        total_cost = 0 
        for cost in self.patients_charges:
            total_cost += float(cost)
        return f"Average Patient Insurance Charge: ${round(total_cost / len(self.patients_charges), 2)}"

    def num_kids_per_patients(self):
        total_num_of_kids = 0 
        for num in self.patients_num_children:
            total_num_of_kids += int(num)
        return f"Average Number of Children per Patient: {round(total_num_of_kids / len(self.patients_num_children), 2)}"

    def num_of_smokers(self):
        total_smokers = 0 
        for status in self.patients_smoker_statuses:
            if status == 'yes':
                total_smokers += 1
        return f"Number of Smokers: {total_smokers} ({round((total_smokers/len(self.patients_smoker_statuses))*100, 1)}%)"

    def smoker_sex(self):
        num_female_smoker = 0 
        num_male_smoker = 0 
        for sex, smoker in zip(self.patients_sexes, self.patients_smoker_statuses):
            if sex == 'female' and smoker == 'yes':
                num_female_smoker += 1
            elif sex == 'male' and smoker == 'yes':
                num_male_smoker += 1
        return f"Female smokers: {num_female_smoker}\nMale smokers: {num_male_smoker}"

    def create_dic(self):
        self.patients_dictionary = {                     
            "ages": [int(age) for age in self.patients_ages],
            "sex": self.patients_sexes,
            "bmi": self.patients_bmis,
            "children": self.patients_num_children,
            "smoker": self.patients_smoker_statuses,
            "regions": self.patients_regions,
            "charges": self.patients_charges
    }
        return self.patients_dictionary


info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

#print(info.avarage_age())
#print(info.sex_count())
#print(info.bmi_average())
#print(info.difference_region())
#print(info.average_cost())
#print(info.num_kids_per_patients())
#print(info.num_of_smokers())
#print(info.smoker_sex())
print(info.create_dic())