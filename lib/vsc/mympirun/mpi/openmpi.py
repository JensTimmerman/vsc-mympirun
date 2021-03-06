##
# Copyright 2009-2012 Ghent University
# Copyright 2009-2012 Stijn De Weirdt
#
# This file is part of VSC-tools,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/VSC-tools
#
# VSC-tools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# VSC-tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with VSC-tools. If not, see <http://www.gnu.org/licenses/>.
##

"""
OpenMPI specific classes
"""

from vsc.mympirun.mpi.mpi import MPI


class OpenMPI(MPI):
    _mpiscriptname_for = ['ompirun']
    _mpirun_for = ['OpenMPI']

    DEVICE_MPIDEVICE_MAP = {'ib':'sm,openib,self', 'det':'sm,tcp,self', 'shm':'sm,self', 'socket':'sm,tcp,self'}

    MPIEXEC_TEMPLATE_GOBAL_OPTION = "--mca %(name)s %(value)s"
    MPIEXEC_TEMPLATE_LOCAL_OPTION = "--mca %(name)s %(value)s"

    MPDBOOT_TEMPLATE_REMOTE_OPTION_NAME = "--mca pls_rsh_agent %(rsh)s"

    def mpiexec_set_global_options(self):
        """Set mpiexec global options"""
        self.mpiexec_global_options['btl'] = self.device

        super(OpenMPI, self).mpiexec_set_global_options()


    def _make_final_mpirun_cmd(self):
        """Create the acual mpirun command
            add it to self.mpirun_cmd
            No mpdboot for openmpi
        """
        self.mpirun_cmd += self.mpiexec_options
