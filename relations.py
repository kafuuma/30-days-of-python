"""course, each course has multiple sections
each section has multiple lecture
lecture model
"""


class Course(models.Model):
    slug = models.charField()
    title = models.charField()
    section = models.ForeignKey(section, on_delete=Cascade)

    def __str__():
        return self.title


class Section(models.Models):
    title = models.charField()
    orders = models.integerField()
    # course = models.ForeignKey(section, on_delete=Cascade)

    # lectures = models.ForeignKey(Lecture, on_delete= cascade)


class Lecture(models.Model):
    title = models.charField()
    order = models.integerField()
    slug = models.charField()
