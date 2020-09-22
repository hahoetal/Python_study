class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop - self.start:
            time = self.start + index
            if time < (23 * 3600) + (59 * 60) + 60:
                return '{0:02d}:{1:02d}:{2:02d}'.format(time // 3600, (time % 3600) // 60, (time % 3600) % 60)
            else:
                time -= (23 * 3600) + (59 * 60) + 60
                return '{0:02d}:{1:02d}:{2:02d}'.format(time // 3600, (time % 3600) // 60, (time % 3600) % 60)

        else: 
            raise IndexError

start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')