def receive(country, city, population=''):
    if population:
        return f"{city.title()},{country.title()}" \
               f" - population {population}"
    else:
        return f"{city.title()},{country.title()}"


class AnonymousSurvey:
    """Collect answer of anonymous survey"""

    def __init__(self, question):
        """Store a question and prepare for storing the answer"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Display questionnaire"""
        print(self.question)

    def store_responses(self, new_responses):
        self.responses.append(new_responses)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"-{response}")


class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raising=5000):
        self.annual_salary += raising
        return self.annual_salary
