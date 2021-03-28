import fluidsynth
import magenta
from magenta.common import merge_hparams
from magenta.contrib import training as contrib_training
from magenta.models.music_vae import data
from magenta.models.music_vae import data_hierarchical
from magenta.models.music_vae import lstm_models
from magenta.models.music_vae.base_model import MusicVAE
import note_seq
import tensorflow
import glob
import collections

# hparams is hyperparameters, increasing free_bits
# and decreasing max_deta creates better replicas but worse random samples
HParams = contrib_training.HParams


# sets up the config class later used to train the model


class Config(collections.namedtuple(
    'Config',
    ['model', 'hparams', 'note_sequence_augmenter',
     'data_converter', 'train_examples_path', 'eval_examples_path',
     'tfds_name'])):
    def values(self):
        return self._asdict()


# sets everything in config to default values
Config.__new__.__defaults__ = (None,) * len(Config._fields)


# allows the config class to update itself
def update_config(config, update_dict):
    config_dict = config.values()
    config_dict.update(update_dict)
    return Config(**config_dict)


CONFIG_MAP = {}

# imports 3 sets of songs from the files in the project
# converts these midi files to note sequences and stores in a list


def import_songs():
    from note_seq.protobuf import music_pb2
    count = 0
    midi1_set = glob.glob("./MidiSet1/*.mid")
    midi2_set = glob.glob("./MidiSet2/*.mid")
    midi3_set = glob.glob("./MidiSet3/*.mid")
    note1_set = []
    note2_set = []
    note3_set = []

    for x in midi1_set:
        sequence = note_seq.midi_file_to_note_sequence(midi1_set[count])
        note1_set.append(sequence)
        # note_seq.play_sequence(sequence, synth=note_seq.synthesize)
        count += 1
    count = 0
    for x in midi2_set:
        sequence = note_seq.midi_file_to_note_sequence(midi2_set[count])
        note2_set.append(sequence)
        # note_seq.play_sequence(sequence, synth=note_seq.synthesize)
        count += 1
    count = 0
    for x in midi3_set:
        sequence = note_seq.midi_file_to_note_sequence(midi3_set[count])
        note3_set.append(sequence)
        # note_seq.play_sequence(sequence, synth=note_seq.synthesize)
        count += 1


# initializes a 16 bar trio model to train
trio_16bar_converter = data.TrioConverter(
    steps_per_quarter=4,
    slice_bars=16,
    gap_bars=2)
# simplest version of the 16 bar trio because it has the largest size
# and I can understand it best
CONFIG_MAP['flat-trio_16bar'] = Config(
    model=MusicVAE(
        lstm_models.BidirectionalLstmEncoder(),
        lstm_models.MultiOutCategoricalLstmDecoder(
            output_depths=[
                90,  # melody
                90,  # bass
                512,  # drums
            ])),
    hparams=merge_hparams(
        lstm_models.get_default_hparams(),
        HParams(
            batch_size=256,
            max_seq_len=256,
            z_size=512,
            enc_rnn_size=[2048, 2048],
            dec_rnn_size=[2048, 2048, 2048],
        )),
    note_sequence_augmenter=None,
    data_converter=trio_16bar_converter,
    train_examples_path='./MidiSet1/',
    eval_examples_path=None,
)


def main():
    # test1()
    import_songs()


if __name__ == '__main__':
    main()
