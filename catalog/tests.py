from django.urls import reverse
from django.test import TestCase

from catalog.models import Mineral


class ViewTesting(TestCase):

    def setUp(self):
        """ Creates two instances of the Mineral Class,
        one that has all its attributes, the other with hardly any.
        """
        # Does not match actual values in app database.
        self.alpha = Mineral.objects.create(
            name="Thaumasite",
            image_filename="240px-Thaumasite.jpg",
            image_caption="Fairfax Quarry, Virginia",
            category="Sulfate",
            formula="<sub>622</sub>.<sub>62</sub> g/mol",
            strunz_classification="07.DG.15",
            color="Colorless, white, pale yellow",
            crystal_system="Hexagonal dipyramidal",
            cleavage="Indistinct",
            mohs_scale_hardness="3.5",
            luster="Vitreous to silky",
            streak="White",
            diaphaneity="Transparent to translucent",
            optical_properties="Uniaxial (-)",
            refractive_index="nω = 1.498–1.507 nε = 1.458–1.470",
            crystal_habit="Prismatic, fibrous, massive, radial",
            specific_gravity="1.877",
            group="Sulfates",
            unit_cell="a = 11.030(7) Å, c = 10.396(6) Å; Z = 2",
            crystal_symmetry="some symmetry",
        )
        # Does not match actual values in app database.
        self.beta = Mineral.objects.create(
            name="Kambaldaite",
            image_filename="240px-Kambaldaite-105011.jpg",
            image_caption="",
            category="",
            formula="",
            strunz_classification="",
            color="",
            crystal_system="",
            cleavage="",
            mohs_scale_hardness="",
            luster="",
            streak="",
            diaphaneity="",
            optical_properties="",
            refractive_index="",
            crystal_habit="",
            specific_gravity="",
            group="",
            unit_cell="",
            crystal_symmetry="",
        )

    def test_if_all_minerals_are_in_index_html(self):
        """ Tests if all minerals within the database
        have their names displayed on the index page.
        """
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/index.html")
        self.assertContains(response, "Thaumasite")
        self.assertContains(response, "Kambaldaite")

    def detail_page_setup(self, mineral_name):
        """ Takes a mineral name within the database and
        assigns its instance to a variable, as well as
        build a response object, both are returned.
        """
        mineral = Mineral.objects.get(name=mineral_name)
        url = reverse("catalog:detail", args=(mineral_name, ))
        response = self.client.get(url)
        return (response, mineral)

    def test_for_all_mineral_attributes_in_detail_html(self):
        """ Tests if a Mineral with all attributes present
        are displayed on its detail page.
        """
        response, mineral = self.detail_page_setup("Thaumasite")
        self.assertTemplateUsed(response, "catalog/detail.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, mineral.name)
        self.assertNotContains(response, mineral.image_filename)
        self.assertContains(response, mineral.formula)
        self.assertContains(response, mineral.category)
        self.assertContains(response, mineral.image_caption)
        self.assertContains(response, mineral.strunz_classification)
        self.assertContains(response, mineral.color)
        self.assertContains(response, mineral.crystal_system)
        self.assertContains(response, mineral.cleavage)
        self.assertContains(response, mineral.mohs_scale_hardness)
        self.assertContains(response, mineral.luster)
        self.assertContains(response, mineral.streak)
        self.assertContains(response, mineral.diaphaneity)
        self.assertContains(response, mineral.optical_properties)
        self.assertContains(response, mineral.optical_properties)
        self.assertContains(response, mineral.refractive_index)
        self.assertContains(response, mineral.crystal_habit)
        self.assertContains(response, mineral.specific_gravity)
        self.assertContains(response, mineral.group)
        self.assertContains(response, mineral.unit_cell)
        self.assertContains(response, mineral.crystal_symmetry)

    def test_for_absent_mineral_attributes_in_detail_html(self):
        """ Tests if a Mineral with many missing values displays
        only those attributes that contain a value.
        """
        response, mineral = self.detail_page_setup("Kambaldaite")
        self.assertTemplateUsed(response, "catalog/detail.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, mineral.name)
        self.assertNotContains(response, mineral.image_filename)

        # If a value were to be missing, & the falsy condition was
        # not functioning the page would contain many <td></td>.
        self.assertNotContains(response, "<td></td>")

    def test_random_view(self):
        """ Tests if the random view properly executes its
        redirect
        """
        response = self.client.get(reverse("catalog:random"))
        self.assertEqual(response.status_code, 302)
