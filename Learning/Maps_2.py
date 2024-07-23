class Graph:
    def __init__(self, dictionary):
        self.graph_dict = dictionary
        # print("Graph Dict:", self.graph_dict)
    #
    # def get_paths(self, start, end, path=[]):
    #     path = path + [start]
    #
    #     if start == end:
    #         return [path]
    #
    #     if start not in self.graph_dict:
    #         return []
    #
    #     paths = []
    #     for node in self.graph_dict[start]:
    #         if node not in path:
    #             new_paths = self.get_paths(node, end, path)
    #             for p in new_paths:
    #                 paths.append(p)
    #
    #     return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


def main():
    routes = [
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    graph = {
        'Andhra Pradesh': {'Karnataka': 580, 'Tamil Nadu': 385, 'Telangana': 256, 'Odisha': 445},
        'Arunachal Pradesh': {'Assam': 370, 'Nagaland': 456},
        'Assam': {'Arunachal Pradesh': 370, 'Meghalaya': 79, 'Nagaland': 324, 'West Bengal': 708},
        'Bihar': {'Jharkhand': 271, 'Uttar Pradesh': 416, 'West Bengal': 570},
        'Chhattisgarh': {'Madhya Pradesh': 485, 'Maharashtra': 527, 'Odisha': 489, 'Telangana': 535},
        'Goa': {'Karnataka': 186, 'Maharashtra': 494},
        'Gujarat': {'Madhya Pradesh': 646, 'Maharashtra': 578, 'Rajasthan': 679},
        'Haryana': {'Delhi': 29, 'Punjab': 201, 'Rajasthan': 301, 'Uttar Pradesh': 190},
        'Himachal Pradesh': {'Punjab': 273, 'Uttarakhand': 351},
        'Jharkhand': {'Bihar': 271, 'Chhattisgarh': 452, 'Odisha': 499, 'West Bengal': 332},
        'Karnataka': {'Andhra Pradesh': 580, 'Goa': 186, 'Kerala': 446, 'Maharashtra': 611, 'Tamil Nadu': 345,
                      'Telangana': 611},
        'Kerala': {'Karnataka': 446, 'Tamil Nadu': 497},
        'Madhya Pradesh': {'Chhattisgarh': 485, 'Gujarat': 646, 'Maharashtra': 600, 'Rajasthan': 486,
                           'Uttar Pradesh': 565},
        'Maharashtra': {'Chhattisgarh': 527, 'Goa': 494, 'Gujarat': 578, 'Karnataka': 611, 'Madhya Pradesh': 600,
                        'Telangana': 563},
        'Manipur': {'Nagaland': 211, 'Mizoram': 264, 'Assam': 479},
        'Meghalaya': {'Assam': 79, 'Tripura': 278},
        'Mizoram': {'Assam': 430, 'Manipur': 264, 'Tripura': 142},
        'Nagaland': {'Arunachal Pradesh': 456, 'Assam': 324, 'Manipur': 211},
        'Odisha': {'Andhra Pradesh': 445, 'Chhattisgarh': 489, 'Jharkhand': 499, 'West Bengal': 482},
        'Punjab': {'Haryana': 201, 'Himachal Pradesh': 273, 'Rajasthan': 367, 'Jammu and Kashmir': 414},
        'Rajasthan': {'Gujarat': 679, 'Haryana': 301, 'Madhya Pradesh': 486, 'Punjab': 367, 'Uttar Pradesh': 520},
        'Sikkim': {'West Bengal': 155},
        'Tamil Nadu': {'Andhra Pradesh': 385, 'Karnataka': 345, 'Kerala': 497},
        'Telangana': {'Andhra Pradesh': 256, 'Chhattisgarh': 535, 'Karnataka': 611, 'Maharashtra': 563},
        'Tripura': {'Assam': 556, 'Meghalaya': 278, 'Mizoram': 142},
        'Uttar Pradesh': {'Bihar': 416, 'Chhattisgarh': 586, 'Delhi': 556, 'Haryana': 190, 'Madhya Pradesh': 565,
                          'Rajasthan': 520, 'Uttarakhand': 274},
        'Uttarakhand': {'Himachal Pradesh': 351, 'Uttar Pradesh': 274},
        'West Bengal': {'Assam': 708, 'Bihar': 570, 'Jharkhand': 332, 'Odisha': 482, 'Sikkim': 155},

        # Union Territories
        'Andaman and Nicobar Islands': {},
        'Chandigarh': {'Haryana': 259, 'Punjab': 238},
        'Dadra and Nagar Haveli and Daman and Diu': {'Gujarat': 398, 'Maharashtra': 171},
        'Delhi': {'Haryana': 29, 'Uttar Pradesh': 556},
        'Jammu and Kashmir': {'Punjab': 414, 'Ladakh': 434},
        'Ladakh': {'Jammu and Kashmir': 434},
        'Lakshadweep': {},
        'Puducherry': {'Tamil Nadu': 160},
    }

    route_graph = Graph(graph)
    start = "Tamil Nadu"
    end = "Jammu and Kashmir"

    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))


if __name__ == '__main__':
    main()
