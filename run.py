import glob
import scheduler

INSTANCE_FOLDER = 'instances'


def main(n=None):
    instance_paths = glob.glob(fr'{INSTANCE_FOLDER}\instance*.py')
    if n is None:
        for instance_path in instance_paths:
            scheduler.main(instance_path)
    else:
        scheduler.main(instance_paths[n])


if __name__ == '__main__':
    main()
