import logging

from django.core.exceptions import MultipleObjectsReturned

from tardis.tardis_portal.models import Schema
from tardis.tardis_portal.models import Dataset_File, DatasetParameterSet

from tardis.tardis_portal.models import Schema, DatafileParameterSet
from tardis.tardis_portal.models import ParameterName, DatafileParameter

logger = logging.getLogger(__name__)

class DicomPngOutput(object):
    def __init__(self, name, schema, tagsToFind=[], tagsToExclude=[]):
        self.name = name
        self.schema = schema
        logger.debug("dicompng __init__")
        logger.debug("dicompng __init__, name: " + str(name))
        logger.debug("dicompng __init__, schema: " + str(schema))

    def __call__(self, sender, **kwargs):
        """post save callback entry point.

        :param sender: The model class.
        :param instance: The actual instance being saved.
        :param created: A boolean; True if a new record was created.
        :type created: bool
        """
        instance = kwargs.get('instance')
        schema = self.getSchema()
        filepath = instance.get_absolute_filepath()

        logger.debug('dicompng filepath: ' + filepath)

        try:
            metadata = self.getDicomMetadata(filepath)

            #previewImage64 = self.getDiffractionPreviewImage(filepath)

            #if previewImage64:
            #    metadata['previewImage'] = previewImage64

            self.saveDicomMetadata(instance, schema, metadata)
        except Exception, e:
            logger.debug(e)
            return None

    def getSchema(self):
        return Schema.objects.get(namespace='http://cai.uq.edu.au/schema/metadata/1')

        # FIXME Ignoring this stuff... why would we dynamically create a Schema here?
        """Return the schema object that the paramaterset will use.
        """
        try:
            return Schema.objects.get(namespace__exact=self.schema)
        except Schema.DoesNotExist:
            schema = Schema(namespace=self.schema, name=self.name,
                            type=Schema.DATAFILE)
            schema.save()
            return schema

    def getDicomMetadata(self, filename):
        import subprocess
        p = subprocess.Popen(['dcmdump', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        # FIXME check stderr
        return stdout

    def saveDicomMetadata(self, instance, schema, metadata):
        """Save all the metadata to a Dataset_Files paramamter set.
        """
        # FIXME reenable this...
        #parameters = self.getParameters(schema, metadata)
        #if not parameters:
        #    logger.debug('dicompng saveDicomMetadata: parameters == NULL :-(')
        #    return None

        logger.debug('dicompng saveDicomMetadata...')

        try:
            ps = DatafileParameterSet.objects.get(schema=schema, dataset_file=instance)
            return ps  # if already exists then just return it
        except DatafileParameterSet.DoesNotExist:
            ps = DatafileParameterSet(schema=schema, dataset_file=instance)
            ps.save()

        logger.debug('dicompng UP TO HERE, WHAT NEXT?')

        # FIXME this line fails due to: /opt/mytardis/tardis-test.log:[10/Jul/2014 15:30:23] DEBUG   dicompng __call__ Cannot assign "'FIXME'": "DatafileParameter.name" must be a "ParameterName" instance.

        dfp = DatafileParameter(parameterset=ps, name=ParameterName.objects.get(name='dump'))
        dfp.string_value = metadata
        dfp.save()

        """
        for p in parameters:
            if p.name in metadata:
                dfp = DatafileParameter(parameterset=ps,
                                        name=p)
                if p.isNumeric():
                    if metadata[p.name] != '':
                        dfp.numerical_value = metadata[p.name]
                        dfp.save()
                else:
                    dfp.string_value = metadata[p.name]
                    dfp.save()
        """

        return ps

def make_filter(name='', schema='', tagsToFind=[], tagsToExclude=[]):
    logger.debug("make_filter dicompng")
    #if not name:
    #    raise ValueError("DicomPngOutput "
    #                     "requires a name to be specified")
    #if not schema:
    #    raise ValueError("DicomPngOutput "
    #                     "requires a schema to be specified")
    return DicomPngOutput(name, schema, tagsToFind, tagsToExclude)

