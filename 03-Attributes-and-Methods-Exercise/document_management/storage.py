class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [c for c in self.categories if c.id == category_id][0]
        category.edit(new_name)

        # for i in range(len(self.categories)):
        #     if self.categories[i].id == category_id:
        #         self.categories[i].name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

        # for i in range(len(self.topics)):
        #     if self.topics[i].id == topic_id:
        #         self.topics[i].topic = new_topic
        #         self.topics[i].storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = [d for d in self.documents if d.id == document_id][0]
        document.edit(new_file_name)

        # for i in range(len((self.documents))):
        #     if self.documents[i].id == document_id:
        #         self.documents[i].file_name = new_file_name

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(category)

        # for i in range(len(self.categories)):
        #     if self.categories[i].id == category_id:
        #         self.categories.remove(self.categories[i])

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(topic)

        # for i in range(len(self.topics)):
        #     if self.topics[i].id == topic_id:
        #         self.topics.remove(self.topics[i])

    def delete_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(document)

        # for i in range(len(self.documents)):
        #     if self.documents[i].id == document_id:
        #         self.documents.remove(self.documents[i])

    def get_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                return d

    def __repr__(self):
        for d in self.documents:
            return repr(d)
