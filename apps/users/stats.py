import matplotlib.pyplot as plt
from django.db.models import Count

# Profile.objects.values('nationality').annotate(Count('nationality'))
# dict = {nat[item]['nationality']:nat[item]['nationality__count'] for item in data]


def get_stats(query):

    # Creates a list of dictionaries of the nationalities and their count
    department_list = query.values("department").annotate(Count("department"))
    program_list = query.values("program").annotate(Count("program"))
    nationality_list = query.values("nationality").annotate(Count("nationality"))

    # Turn the list of dictionaries into one dictionary
    department = {item["department"]: item["department__count"] for item in department_list}
    program = {item["program"]: item["program__count"] for item in program_list}
    nationality = {item["nationality"]: item["nationality__count"] for item in nationality_list}

    # Call the plotting function (used in case the plotting function wants to be changed)
    plots = [make_plot(department, "department"), make_plot(program, "program"), make_plot(nationality, "nationality")]
    return plots


def make_plot(data, name):
    # Makes a plot from the data and then returns the location of where it's saved
    filepath = "/tmp/" + name + "-graph.jpg"
    plt.figure(1, [20, 8])
    plt.bar(data.keys(), data.values())
    plt.title(name.capitalize())
    plt.savefig(filepath)
    plt.close()

    return filepath
