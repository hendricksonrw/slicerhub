from slic3rwrap import Slic3rWrappers

class SlicerFactory():

    SLIC3R='Slic3r'

    @staticmethod
    def create_slicer(slicer, version):
        """This is a factory to create the appropriate slicer to slice the model
        with. It will allow a by slicer by version filter to function"""

        # Slic3r
        if slicer == 'Slic3r':
            return Slic3rWrappers.create_slicer(version)

        # Skienforge
        # Cura
        return None
