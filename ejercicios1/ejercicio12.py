
class Computer:
    def __init__(self, size, storage):
        self.size = size
        self.storage = storage
    
    def print_specs(self):
        print(f"Display size: {self.size}")
        print(f"Storage size: {self.storage}")

low_spec = Computer("13","256GB")
high_spec = Computer("27", "1TB")

print("Low Spec Computer:")
low_spec.print_specs()

print("High Spec Computer:")
high_spec.print_specs()     


"""
Low Spec Computer:
Display size: 13   
Storage size: 256GB
High Spec Computer:
Display size: 27   
Storage size: 1TB 
"""