from collections import namedtuple

DataIngestionArtifact =namedtuple("DataIngestionArtifact",["train_filepath", "test_file_path","is_ingested","message"])
